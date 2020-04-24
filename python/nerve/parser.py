from copy import copy
from pyparsing import delimitedList, Group, Optional, Or, ParseException, Regex, Suppress
# ------------------------------------------------------------------------------


class AssetNameParser:
    '''
    A class for converting asset names to metadata and metadata to asset names,
    according to a dynimcally defined grammar.
    '''
    FIELD_SEPARATOR = '_'
    TOKEN_SEPARATOR = '-'
    PROJECT_INDICATOR = 'p' + TOKEN_SEPARATOR
    SPECIFICATION_INDICATOR = 's' + TOKEN_SEPARATOR
    DESCRIPTOR_INDICATOR = 'd' + TOKEN_SEPARATOR
    VERSION_INDICATOR = 'v'
    COORDINATE_INDICATOR = 'c'
    FRAME_INDICATOR = 'f'
    EXTENSION_INDICATOR = '.'
    LEGAL_FIELDS = [
        'project',
        'specification',
        'descriptor',
        'version',
        'coordinate',
        'frame',
        'extension'
    ]

    VERSION_PADDING = 3
    COORDINATE_PADDING = 3
    FRAME_PADDING = 4

    def __init__(self, fields):
        '''
        Create a AssetNameParser instance with given fields.

        Args:
            fields (list[str]): An ordered list of asset fields.

        Raises:
            ValueError: If fields is empty.
            ValueError: If fields are duplicated.
            ValueError: If illegal fields are given.
            ValueError: If illegal field order given.

        Returns:
            AssetNameParser: instance.
        '''
        # ensure fields is not empty
        if len(fields) == 0:
            msg = 'Fields cannot be empty.'
            raise ValueError(msg)

        # ensure fields are ot duplicated
        if len(fields) != len(set(fields)):
            msg = 'Fields cannot contain duplicates.'
            raise ValueError(msg)

        # ensure fields are legal
        illegal_fields = list(filter(lambda x: x not in self.LEGAL_FIELDS, fields))
        if len(illegal_fields) > 0:
            msg = f'Illegal fields found: {illegal_fields}. '
            msg += f'Legal fields include: {self.LEGAL_FIELDS}.'
            raise ValueError(msg)

        # ensure extension is last field
        if 'extension' in fields and fields[-1] != 'extension':
            msg = 'Illegal field order: Extension field must be last if it is '
            msg += 'included in fields.'
            raise ValueError(msg)

        grammar = self._get_grammar()
        self._extension_parser = self._get_extension_parser(grammar)
        self._ordered_parser = self._get_ordered_parser(grammar, fields)
        self._unordered_parser = self._get_unordered_parser(grammar, fields)
        self._fields = fields

    # GRAMMAR-------------------------------------------------------------------
    @staticmethod
    def _raise_field_error(field, part):
        '''
        A convenience function used for raising custom ParseExceptions.

        Args:
            field (str): Field.
            part (str): Part of field.

        Returns:
            function: lambda s, l, i, e: raise_error(field, s, i)
        '''
        def raise_error(field, text, instance):
            expr = None
            if hasattr(instance, 'expr'):
                expr = instance.expr
            else:
                expr = instance.pattern

            msg = f'Illegal {field} field {part} in "{text}". '
            msg += f'Expecting: {expr}'
            raise ParseException(msg)
        return lambda s, l, i, e: raise_error(field, s, i)

    @staticmethod
    def _get_grammar():
        '''
        Create parser grammar dictionary.

        Returns:
            dict: Grammar.
        '''
        project = Regex(r'[a-z]{3,4}\d{1,3}')\
            .setResultsName('project')\
            .setFailAction(AssetNameParser._raise_field_error('project', 'token'))

        specification = Regex(r'[a-z]{3,4}\d\d\d')\
            .setResultsName('specification')\
            .setFailAction(AssetNameParser._raise_field_error('specification', 'token'))

        descriptor = Regex(r'[a-z0-9][a-z0-9-]*')\
            .setResultsName('descriptor')\
            .setFailAction(AssetNameParser._raise_field_error('descriptor', 'token'))

        version = Regex(r'\d{' + str(AssetNameParser.VERSION_PADDING) + '}')\
            .setParseAction(lambda s, l, t: int(t[0]))\
            .setResultsName('version')\
            .setFailAction(AssetNameParser._raise_field_error('version', 'token'))

        coord = Regex(r'\d{' + str(AssetNameParser.COORDINATE_PADDING) + '}')\
            .setParseAction(lambda s, l, t: int(t[0]))
        t_sep = Suppress(AssetNameParser.TOKEN_SEPARATOR)
        coordinate = Group(coord + Optional(t_sep + coord) + Optional(t_sep + coord))\
            .setResultsName('coordinate')\
            .setFailAction(AssetNameParser._raise_field_error('coordinate', 'token'))

        frame = Regex(r'\d{' + str(AssetNameParser.FRAME_PADDING) + '}')\
            .setParseAction(lambda s, l, t: int(t[0]))\
            .setResultsName('frame')\
            .setFailAction(AssetNameParser._raise_field_error('frame', 'token'))

        extension = Regex(r'[a-zA-Z0-9]+$')\
            .setResultsName('extension')\
            .setFailAction(AssetNameParser._raise_field_error('extension', 'token'))
        # ----------------------------------------------------------------------

        project_indicator = Suppress(AssetNameParser.PROJECT_INDICATOR)\
            .setFailAction(AssetNameParser._raise_field_error('project', 'indicator'))

        specification_indicator = Suppress(AssetNameParser.SPECIFICATION_INDICATOR)\
            .setFailAction(AssetNameParser._raise_field_error('specification', 'indicator'))

        descriptor_indicator = Suppress(AssetNameParser.DESCRIPTOR_INDICATOR)\
            .setFailAction(AssetNameParser._raise_field_error('descriptor', 'indicator'))

        version_indicator = Suppress(AssetNameParser.VERSION_INDICATOR)\
            .setFailAction(AssetNameParser._raise_field_error('version', 'indicator'))

        coordinate_indicator = Suppress(AssetNameParser.COORDINATE_INDICATOR)\
            .setFailAction(AssetNameParser._raise_field_error('coordinate', 'indicator'))

        frame_indicator = Suppress(AssetNameParser.FRAME_INDICATOR)\
            .setFailAction(AssetNameParser._raise_field_error('frame', 'indicator'))

        extension_indicator = Suppress(AssetNameParser.EXTENSION_INDICATOR)\
            .setFailAction(AssetNameParser._raise_field_error('extension', 'indicator'))
        # ----------------------------------------------------------------------

        grammar = {
            'project': project_indicator + project,
            'specification': specification_indicator + specification,
            'specification_token': specification,
            'descriptor': descriptor_indicator + descriptor,
            'version': version_indicator + version,
            'coordinate': coordinate_indicator + coordinate,
            'frame': frame_indicator + frame,
            'extension': extension_indicator + extension,
            'extension_token': extension,
            'field_separator': Suppress(AssetNameParser.FIELD_SEPARATOR)
        }
        return grammar

    # PARSERS-------------------------------------------------------------------
    @staticmethod
    def _get_extension_parser(grammar):
        '''
        Creates a parser for file extensions.

        Args:
            grammar (dict): AssetNameParser grammar dictionary.

        Returns:
            Group: Parser.
        '''
        parser = Optional(Suppress(Regex(r'.*\.|.*?'))) + grammar['extension_token']
        parser = Group(parser)
        return parser

    @staticmethod
    def _get_unordered_parser(grammar, fields):
        '''
        Creates a parser for asset names of fields with arbitrary order.

        Args:
            grammar (dict): AssetNameParser grammar dictionary.
            fields (list[str]): List of fields.

        Returns:
            Group: Parser.
        '''
        # TODO: fix grammar so that there are no duplicate field matches.
        parser = None
        if fields[-1] == 'extension':
            field = Or([grammar[x] for x in fields[:-1]])
            parser = delimitedList(field, delim=grammar['field_separator'])
            parser += grammar[fields[-1]]
        else:
            field = Or([grammar[x] for x in fields])
            parser = delimitedList(field, delim=grammar['field_separator'])

        parser = Group(parser)
        return parser

    @staticmethod
    def _get_ordered_parser(grammar, fields):
        '''
        Creates a parser for asset names.

        Args:
            grammar (dict): AssetNameParser grammar dictionary.
            fields (list[str]): List of fields.

        Returns:
            Group: Parser.
        '''
        parser = Suppress(Regex('^'))
        for i, field in enumerate(fields[:-1]):
            parser += grammar[field]
            if fields[i + 1] != 'extension':
                parser += grammar['field_separator']
        parser += grammar[fields[-1]]
        parser += Suppress(Regex('$'))
        parser = Group(parser)
        return parser

    @staticmethod
    def _get_specification_parser():
        '''
        Returns a parser for finding a specification within an arbitrary string.

        Returns:
            Group: Parser.
        '''
        grammar = AssetNameParser._get_grammar()
        indicator = Suppress(Regex('.*' + AssetNameParser.SPECIFICATION_INDICATOR))
        parser = indicator + grammar['specification_token']
        parser = Group(parser)
        return parser

    # PUBLIC--------------------------------------------------------------------
    @staticmethod
    def parse_specification(text):
        '''
        Parse a string for a specification.

        Args:
            text (str): String to be parsed.

        Raises:
            ParseException: If specification is not found.

        Returns:
            dict: Dictionary with "specification" key.
        '''
        try:
            return AssetNameParser\
                ._get_specification_parser()\
                .parseString(text)[0].asDict()
        except ParseException:
            msg = f'Specification not found in "{text}".'
            raise ParseException(msg)

    def parse(self, text, ignore_order=False):
        '''
        Create a parser based on the given fields.

        Args:
            fields (list[str]): A list of fields.
            ignore_order (bool, optional): Whether to ignore the field order.
                Default: False.

        Returns:
            Group: parser.
        '''
        if self._fields == ['extension']:
            return self._extension_parser.parseString(text)[0].asDict()

        # parse text
        if ignore_order:
            return self._unordered_parser.parseString(text)[0].asDict()

        else:
            # determine if the text can be parsed with random field order
            try:
                self._unordered_parser.parseString(text)
                parsable = True
            except ParseException:
                parsable = False

            try:
                return self._ordered_parser.parseString(text)[0].asDict()
            except ParseException as msg:
                # it is a field order error if it is parasable with a different
                # field order
                if parsable:
                    msg = f'Incorrect field order in "{text}". '
                    msg += f'Given field order: {self._fields}.'
                raise ParseException(msg)

    def to_string(self, dict_):
        '''
        Converts a given dictionary to a string.

        Args:
            dict_ (dict): Dictionary.

        Returns:
            str: Asset name.
        '''
        fields = copy(self._fields)
        has_extension = False
        if fields[-1] == 'extension':
            has_extension = True
            fields.pop()

        output = []
        for field in fields:
            if field in dict_.keys():
                indicator = getattr(self, field.upper() + '_INDICATOR')

                token = dict_[field]
                if field == 'version':
                    token = str(token).zfill(self.VERSION_PADDING)

                elif field == 'coordinate':
                    token = [str(x).zfill(self.COORDINATE_PADDING) for x in token]
                    token = self.TOKEN_SEPARATOR.join(token)

                elif field == 'frame':
                    token = str(token).zfill(self.FRAME_PADDING)

                output.append(indicator + token)
        output = self.FIELD_SEPARATOR.join(output)

        if has_extension:
            output += self.EXTENSION_INDICATOR + dict_['extension']
        return output

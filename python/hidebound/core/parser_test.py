import unittest
from pyparsing import ParseException, Regex
from hidebound.core.parser import AssetNameParser
# ------------------------------------------------------------------------------


class ParserTests(unittest.TestCase):
    fields = [
        'project', 'specification', 'descriptor', 'version', 'coordinate', 'frame', 'extension'
    ]

    def test_init(self):
        with self.assertRaisesRegexp(ValueError, 'Fields cannot be empty.'):
            AssetNameParser([])

        with self.assertRaisesRegexp(ValueError, 'Fields cannot contain duplicates.'):
            AssetNameParser(['foo', 'foo'])

        with self.assertRaisesRegexp(ValueError, r"Illegal fields found: \['foo', 'bar'\]"):
            AssetNameParser(['project', 'specification', 'foo', 'bar'])

        err = 'Illegal field order: Extension field must be last if it is included in fields.'
        with self.assertRaisesRegexp(ValueError, err):
            AssetNameParser(['project', 'specification', 'extension', 'descriptor'])

        fields = ['project', 'specification', 'version']
        result = AssetNameParser(fields)
        self.assertEqual(result._fields, fields)

        fields = ['specification', 'version', 'project', 'frame']
        result = AssetNameParser(fields)
        self.assertEqual(result._fields, fields)

    def test_raise_field_error(self):
        parser = Regex(r'foo')\
            .setFailAction(AssetNameParser._raise_field_error('foo', 'bar'))
        expected = 'Illegal foo field bar in "baz". Expecting: foo'
        with self.assertRaisesRegexp(ParseException, expected):
            parser.parseString('baz')

    def test_parse_0(self):
        name = 'p-proj001_s-spec002_d-desc_v003_c0004-0005-0006_f0007.exr'
        result = AssetNameParser(self.fields).parse(name)
        expected = dict(
            project='proj001',
            specification='spec002',
            descriptor='desc',
            version=3,
            coordinate=[4, 5, 6],
            frame=7,
            extension='exr'
        )
        self.assertEqual(result, expected)

    def test_parse_1(self):
        fields = [
            'project', 'specification', 'descriptor', 'version', 'frame',
            'extension'
        ]
        name = 'p-proj002_s-spec062_d-desc_v099_f0078.exr'
        result = AssetNameParser(fields).parse(name)
        expected = dict(
            project='proj002',
            specification='spec062',
            descriptor='desc',
            version=99,
            frame=78,
            extension='exr',
        )
        self.assertEqual(result, expected)

    def test_parse_2(self):
        fields = ['project', 'specification', 'coordinate', 'version']
        name = 'p-proj002_s-spec062_c0000-0000-0000_v099'
        result = AssetNameParser(fields).parse(name)
        expected = dict(
            project='proj002',
            specification='spec062',
            version=99,
            coordinate=[0, 0, 0]
        )
        self.assertEqual(result, expected)

    def test_parse_bad_order(self):
        fields = [
            'project', 'specification', 'descriptor', 'version', 'frame',
            'extension'
        ]
        name = 's-spec062_p-proj002_v099_d-desc_f0078.exr'
        with self.assertRaises(ParseException):
            AssetNameParser(fields).parse(name)

    def test_parse_bad_indicator(self):
        fields = [
            'project', 'specification', 'descriptor', 'version', 'frame',
            'extension'
        ]
        name = 'p-proj002_s-spec062_f-desc_v099_f0078.exr'
        msg = f'Illegal descriptor field indicator in "{name}". Expecting: "d-"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(fields).parse(name)

        name = 'pp-proj002_s-spec062_d-desc_v099_f0078.exr'
        msg = f'Illegal project field indicator in "{name}". Expecting: "p-"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(fields).parse(name)

    def test_parse_bad_token(self):
        fields = [
            'project', 'specification', 'descriptor', 'version', 'frame',
            'extension'
        ]
        name = 'p-proj002_s-spec062_d-HELLO_v099_f0078.exr'
        msg = f'Illegal descriptor field token in "{name}". Expecting: .*'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(fields).parse(name)

    def test_to_string(self):
        fields = [
            'project', 'specification', 'descriptor', 'version', 'coordinate',
            'frame', 'extension'
        ]
        metadata = dict(
            project='proj002',
            specification='spec062',
            descriptor='desc',
            version=99,
            coordinate=[1, 2, 3],
            frame=78,
            extension='exr',
            foo='bar'
        )
        result = AssetNameParser(fields).to_string(metadata)
        expected = 'p-proj002_s-spec062_d-desc_v099_c0001-0002-0003_f0078.exr'
        self.assertEqual(result, expected)

    def test_recurse_init(self):
        fields = [
            'project', 'specification', 'descriptor', 'version', 'frame',
            'extension'
        ]
        expected = 'p-proj002_s-spec062_d-desc_v099_f0078.exr'
        parser = AssetNameParser(fields)
        result = parser.parse(expected)
        result = parser.to_string(result)
        self.assertEqual(result, expected)

    # PROJECT-------------------------------------------------------------------
    def test_parse_project_single_field(self):
        name = 'p-proj001'
        result = AssetNameParser(['project']).parse(name)
        expected = dict(project='proj001')
        self.assertEqual(result, expected)

    def test_parse_project_indicator(self):
        name = 'pr-proj001_s-spec002_d-desc_v003_c0004-0005-0006_f0007.exr'
        msg = f'Illegal project field indicator in "{name}". Expecting: "p-"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    def test_parse_project_token(self):
        name = 'p-proj-001_s-spec002_d-desc_v003_c0004-0005-0006_f0007.exr'
        msg = f'Illegal project field token in "{name}". Expecting: .*'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    # SPECIFICATION-------------------------------------------------------------
    def test_parse_specification_single_field(self):
        name = 's-spec002'
        result = AssetNameParser(['specification']).parse(name)
        expected = dict(specification='spec002')
        self.assertEqual(result, expected)

    def test_parse_specification_indicator(self):
        name = 'p-proj001_sspec002_d-desc_v003_c0004-0005-0006_f0007.exr'
        msg = f'Illegal specification field indicator in "{name}". Expecting: "s-"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    def test_parse_specification_token(self):
        name = 'p-proj001_s-002spec_d-desc_v003_c0004-0005-0006_f0007.exr'
        msg = f'Illegal specification field token in "{name}". Expecting: .*'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    # DESCRIPTOR----------------------------------------------------------------
    def test_parse_descriptor_single_field(self):
        name = 'd-desc003'
        result = AssetNameParser(['descriptor']).parse(name)
        expected = dict(descriptor='desc003')
        self.assertEqual(result, expected)

    def test_parse_descriptor_containing_indicators(self):
        name = 'p-proj001_s-spec002_d-v012-p-banana-f99_v003_c0004-0005-0006_f0007.exr'
        result = AssetNameParser(self.fields).parse(name)['descriptor']
        expected = 'v012-p-banana-f99'
        self.assertEqual(result, expected)

    def test_parse_descriptor_indicator(self):
        name = 'p-proj001_s-spec002_ddesc_v003_c0004-0005-0006_f0007.exr'
        msg = f'Illegal descriptor field indicator in "{name}". Expecting: "d-"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    def test_parse_descriptor_token(self):
        name = 'p-proj001_s-spec002_d-DeSC_v003_c0004-0005-0006_f0007.exr'
        msg = f'Illegal descriptor field token in "{name}". Expecting: .*'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    # VERSION-------------------------------------------------------------------
    def test_parse_version_single_field(self):
        name = 'v003'
        result = AssetNameParser(['version']).parse(name)
        expected = dict(version=3)
        self.assertEqual(result, expected)

    def test_parse_version_indicator(self):
        name = 'p-proj001_s-spec002_d-desc_b003_c0004-0005-0006_f0007.exr'
        msg = f'Illegal version field indicator in "{name}". Expecting: "v"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    def test_parse_version_token(self):
        name = 'p-proj001_s-spec002_d-desc_v03_c0004-0005-0006_f0007.exr'
        msg = f'Illegal version field token in "{name}". Expecting: .*'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

        name = 'p-proj001_s-spec002_d-desc_v03'
        msg = f'Illegal version field token in "{name}". Expecting: .*'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields[:-3]).parse(name)

    # COORDINATE----------------------------------------------------------------
    def test_parse_coordinate_single_field(self):
        name = 'c0004-0005-0006'
        result = AssetNameParser(['coordinate']).parse(name)
        expected = dict(coordinate=[4, 5, 6])
        self.assertEqual(result, expected)

    def test_parse_coordinate_indicator(self):
        name = 'p-proj001_s-spec002_d-desc_v003_x004-005-006_f0007.exr'
        msg = f'Illegal coordinate field indicator in "{name}". Expecting: "c"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

        name = 'p-proj001_s-spec002_d-desc_v003_x004-y005-z006_f0007.exr'
        msg = f'Illegal coordinate field indicator in "{name}". Expecting: "c"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    def test_parse_coordinate_token(self):
        name = 'p-proj001_s-spec002_d-desc_v003_c05-06_f0007.exr'
        msg = f'Illegal coordinate field token in "{name}". Expecting: .*'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    # FRAME---------------------------------------------------------------------
    def test_parse_frame_single_field(self):
        name = 'f0007'
        result = AssetNameParser(['frame']).parse(name)
        expected = dict(frame=7)
        self.assertEqual(result, expected)

    def test_parse_frame_indicator(self):
        name = 'p-proj001_s-spec002_d-desc_v003_c0004-0005-0006_0007.exr'
        msg = f'Illegal frame field indicator in "{name}". Expecting: "f"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

        name = 'p-proj001_s-spec002_d-desc_v003_c0004-0005-0006_#0007.exr'
        msg = f'Illegal frame field indicator in "{name}". Expecting: "f"'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    def test_parse_frame_token(self):
        name = 'p-proj001_s-spec002_d-desc_v003_c0004-0005-0006_f007.exr'
        msg = f'Illegal frame field token in "{name}". Expecting: .*'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    # EXTENSION-----------------------------------------------------------------
    def test_parse_extension_single_field(self):
        name = 'exr'
        result = AssetNameParser(['extension']).parse(name)
        expected = dict(extension='exr')
        self.assertEqual(result, expected)

    def test_parse_extension_uppercase(self):
        fields = ['descriptor', 'extension']
        name = 'd-desc.EXR'
        expected = dict(descriptor='desc', extension='EXR')
        result = AssetNameParser(fields).parse(name)
        self.assertEqual(result, expected)

    def test_parse_extension_indicator(self):
        name = 'p-proj001_s-spec002_d-desc_v003_c0004-0005-0006_f0007_exr'
        msg = f'Illegal extension field indicator in "{name}". Expecting: "."'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    def test_parse_extension_token(self):
        name = 'p-proj001_s-spec002_d-desc_v003_c0004-0005-0006_f0007.@!#'
        msg = f'Illegal extension field token in "{name}". Expecting: .*'
        with self.assertRaisesRegexp(ParseException, msg):
            AssetNameParser(self.fields).parse(name)

    # GRAMMAR-------------------------------------------------------------------
    def test_get_grammar(self):
        result = AssetNameParser._get_grammar()
        expected = [
            'project',
            'specification',
            'descriptor',
            'version',
            'coordinate',
            'frame',
            'extension',
            'field_separator',
        ]
        result = set(expected).difference(result.keys())
        self.assertEqual(len(result), 0)

    def test_get_extension_parser(self):
        grammar = AssetNameParser._get_grammar()
        parser = AssetNameParser._get_extension_parser(grammar)

        expected = 'Illegal extension field token.*'
        with self.assertRaisesRegexp(ParseException, expected):
            parser.parseString('foo.')

        expected = 'Illegal extension field token.*'
        with self.assertRaisesRegexp(ParseException, expected):
            parser.parseString('foo.bar-baz')

        result = parser.parseString('foo.bar')[0].asDict()['extension']
        self.assertEqual(result, 'bar')

        result = parser.parseString('foo.bar.baz')[0].asDict()['extension']
        self.assertEqual(result, 'baz')

        result = parser.parseString('foo')[0].asDict()['extension']
        self.assertEqual(result, 'foo')

        result = parser.parseString('.foo')[0].asDict()['extension']
        self.assertEqual(result, 'foo')

    def test_get_parser(self):
        fields = [
            'project', 'specification', 'descriptor', 'version', 'coordinate',
            'frame', 'extension'
        ]
        grammar = AssetNameParser._get_grammar()
        parser = AssetNameParser._get_parser(grammar, fields)

        expected = dict(
            project='proj001',
            specification='spec002',
            descriptor='desc',
            version=3,
            coordinate=[4, 5, 6],
            frame=7,
            extension='exr'
        )
        name = 'p-proj001_s-spec002_d-desc_v003_c0004-0005-0006_f0007.exr'
        result = parser.parseString(name)[0].asDict()
        self.assertEqual(result, expected)

        name = 'p-proj001.s-spec002.d-desc.v003.c0004-0005-0006.f0007.exr'
        with self.assertRaises(ParseException):
            parser.parseString(name)[0].asDict()

        # no extension
        parser = AssetNameParser._get_parser(grammar, fields[:-1])
        del expected['extension']
        name = 'p-proj001_s-spec002_d-desc_v003_c0004-0005-0006_f0007'
        result = parser.parseString(name)[0].asDict()
        self.assertEqual(result, expected)

        name = 'p-proj001_s-spec002_d-desc_v003_c0004-0005-0006_f0007_exr'
        with self.assertRaises(ParseException):
            parser.parseString(name)[0].asDict()

    def test_get_specification_parser(self):
        parser = AssetNameParser._get_specification_parser()
        expected = dict(specification='spec001')

        names = [
            's-spec001',
            'p-s-spec001',
            'pizzas-spec001',
            'pizza_s-spec001',
            's-spec001banana',
            's-spec0012',
            'p-proj001_s-spec001_d-desc_v001',
            'p-proj001_s-spec001_d-descs-123_v001',
            'p-proj001_s-spec001_d-desc-s-123_v001',
        ]
        for name in names:
            result = parser.parseString(name)[0].asDict()
            self.assertEqual(result, expected)

        names = [
            'spec001',
            '-spec001',
            'p-spec001',
            's.spec001',
            's-001spec',
            's-sp001',
            's-specification001'
        ]
        for name in names:
            with self.assertRaises(ParseException):
                parser.parseString(name)[0].asDict()

    def test_parse_specification(self):
        expected = dict(specification='spec001')
        result = AssetNameParser.parse_specification('s-spec001')
        self.assertEqual(result, expected)

        expected = 'Specification not found in "spec001".'
        with self.assertRaisesRegexp(ParseException, expected):
            AssetNameParser.parse_specification('spec001')

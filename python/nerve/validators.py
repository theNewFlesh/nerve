'''
The validators module is function library for validating singular traits given
to a specification.

Validators are linked with traits via the validators kwarg of a
specification class attribute. They succeed silently and raise DataError when
the trait they validate fails. Schematics captures these error messages and
pipes them to an error call.
'''

import re

from pyparsing import ParseException
import wrapt

from nerve.parser import AssetNameParser
# ------------------------------------------------------------------------------


class ValidationError(Exception):
    '''Error raised for validators.'''
    pass


def validator(message):
    '''
    A decorator for predicate functions that raises a ValidationError
    if it returns False.

    Args:
        message (str): Error message if predicate returns False.

    Raises:
        ValidationError: If predicate returns False.

    Returns:
        function: Function that returns a boolean.
    '''
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        if not wrapped(*args):
            args = [str(x) for x in args] * 10
            msg = message.format(*args)
            raise ValidationError(msg)
        return
    return wrapper


@validator('"{}" is not a valid project name.')
def is_project(item):
    '''
    Validates a project name.

    Args:
        item (str): Project name.

    Raises:
        ValidationError: If project name is invalid.

    Returns:
        bool: Validity of project name.
    '''
    try:
        ind = AssetNameParser.PROJECT_INDICATOR
        AssetNameParser(['project']).parse(ind + item)
    except ParseException:
        return False

    if re.search('^[a-z0-9]+$', item) is None:
        return False

    return True


@validator('"{}" is not a valid descriptor.')
def is_descriptor(item):
    '''
    Validates a descriptor.

    Args:
        item (str): Descriptor.

    Raises:
        ValidationError: If descriptor is invalid.

    Returns:
        bool: Validity of descriptor.
    '''
    try:
        ind = AssetNameParser.DESCRIPTOR_INDICATOR
        AssetNameParser(['descriptor']).parse(ind + item)
    except ParseException:
        return False

    if re.search('^[a-z0-9-]+$', item) is None:
        return False

    # the mast/final/last asset is never actually that
    # asset should only ever be thought of in terms of latest version
    if re.search('^(master|final|last)', item):
        return False

    if len(item) < 1:
        return False

    return True


@validator('{} is not a valid version. 0 < version < 1000.')
def is_version(item):
    '''
    Validates a version.

    Args:
        item (str): Version.

    Raises:
        ValidationError: If version is invalid.

    Returns:
        bool: Validity of version.
    '''
    return item > 0 and item < 10**AssetNameParser.VERSION_PADDING


@validator('{} is not a valid frame. -1 < frame < 10000.')
def is_frame(item):
    '''
    Validates a frame.

    Args:
        item (str): Frame.

    Raises:
        ValidationError: If frame is invalid.

    Returns:
        bool: Validity of frame.
    '''
    return item >= 0 and item < 10**AssetNameParser.FRAME_PADDING


@validator('{} is not a valid coordinate. -1 < coordinate < 1000.')
def is_coordinate(item):
    '''
    Validates a coordinate.

    Args:
        item (str): Coordinate.

    Raises:
        ValidationError: If coordinate is invalid.

    Returns:
        bool: Validity of coordinate.
    '''
    if len(item) == 0:
        return False

    if len(item) > 3:
        return False

    if min(item) < 0:
        return False

    if max(item) >= 10**AssetNameParser.COORDINATE_PADDING:
        return False

    return True


@validator('"{}" is not a valid extension.')
def is_extension(item):
    '''
    Validates a file extension.

    Args:
        item (str): File extension.

    Raises:
        ValidationError: If extension is invalid.

    Returns:
        bool: Validity of extension.
    '''
    if re.search('^[a-z0-9]+$', item):
        return True
    return False


@validator('{} != {}.')
def is_eq(a, b):
    '''
    Validates that a and b are equal.

    Args:
        a (object): Object.
        b (object): Object.

    Raises:
        ValidationError: If a does not equal b.

    Returns:
        bool: Equality of a and b.
    '''
    return a == b


@validator('{} !< {}.')
def is_lt(a, b):
    '''
    Validates that a is less than b.

    Args:
        a (object): Object.
        b (object): Object.

    Raises:
        ValidationError: If a is not less than b.

    Returns:
        bool: A is less than b.
    '''
    return a < b


@validator('{} !> {}.')
def is_gt(a, b):
    '''
    Validates that a is greater than b.

    Args:
        a (object): Object.
        b (object): Object.

    Raises:
        ValidationError: If a is not greater than b.

    Returns:
        bool: A is greater than b.
    '''
    return a > b
from typing import Any, Callable, List, Union

from collections import Counter
from itertools import product
from pathlib import Path
import os
import re

from pandas import DataFrame
from pyparsing import ParseException
from schematics.exceptions import ValidationError
import wrapt

from hidebound.core.parser import AssetNameParser
# ------------------------------------------------------------------------------


'''
The validators module is function library for validating singular traits given
to a specification.

Validators are linked with traits via the validators kwarg of a
specification class attribute. They succeed silently and raise DataError when
the trait they validate fails. Schematics captures these error messages and
pipes them to an error call.
'''


def validate(message):
    # type: (str) -> Callable
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


def validate_each(message, list_first_arg=False):
    # type: (str, bool) -> Callable
    '''
    A decorator for predicate functions that raises a ValidationError
    if it returns False when applied to each argument individually.

    Args:
        message (str): Error message if predicate returns False.
        list_first_arg (str, optional): Set to True if first argument is a list.
            Default: False.

    Raises:
        ValidationError: If predicate returns False.

    Returns:
        function: Function that returns a boolean.
    '''
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        extra_args = []
        if len(args) > 1:
            extra_args = args[1:]

        args = args[0]
        if list_first_arg or not isinstance(args, list):
            args = [args]
        for arg in args:
            if not wrapped(arg, *extra_args):
                msg = message.format(arg, *extra_args)
                raise ValidationError(msg)
        return
    return wrapper


# VALIDATORS--------------------------------------------------------------------
@validate_each('"{}" is not a valid project name.')
def is_project(item):
    # type: (str) -> bool
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
        return False  # pragma: no cover

    if re.search('^[a-z0-9]+$', item) is None:
        return False  # pragma: no cover

    return True


@validate_each('"{}" is not a valid descriptor.')
def is_descriptor(item):
    # type: (str) -> bool
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
        return False  # pragma: no cover

    if re.search('^[a-z0-9-]+$', item) is None:
        return False  # pragma: no cover

    # the mast/final/last asset is never actually that
    # asset should only ever be thought of in terms of latest version
    if re.search('^(master|final|last)', item):
        return False  # pragma: no cover

    if len(item) < 1:
        return False  # pragma: no cover

    return True


@validate_each('{} is not a valid version. 0 < version < 1000.')
def is_version(item):
    # type: (int) -> bool
    '''
    Validates a version.

    Args:
        item (int): Version.

    Raises:
        ValidationError: If version is invalid.

    Returns:
        bool: Validity of version.
    '''
    return item > 0 and item < 10**AssetNameParser.VERSION_PADDING


@validate_each('{} is not a valid frame. -1 < frame < 10000.')
def is_frame(item):
    # type: (int) -> bool
    '''
    Validates a frame.

    Args:
        item (int): Frame.

    Raises:
        ValidationError: If frame is invalid.

    Returns:
        bool: Validity of frame.
    '''
    return item >= 0 and item < 10**AssetNameParser.FRAME_PADDING


@validate_each(
    '{} is not a valid coordinate. -1 < coordinate < 1000.',
    list_first_arg=True
)
def is_coordinate(item):
    # type: (List[int]) -> bool
    '''
    Validates a coordinate.

    Args:
        item (list[int]): Coordinate.

    Raises:
        ValidationError: If coordinate is invalid.

    Returns:
        bool: Validity of coordinate.
    '''
    if len(item) == 0:
        return False  # pragma: no cover

    if len(item) > 3:
        return False  # pragma: no cover

    if min(item) < 0:
        return False  # pragma: no cover

    if max(item) >= 10**AssetNameParser.COORDINATE_PADDING:
        return False  # pragma: no cover

    return True


@validate_each('"{}" is not a valid extension.')
def is_extension(item):
    # type: (str) -> bool
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
    return False  # pragma: no cover


@validate_each('{} != {}.')
def is_eq(a, b):
    # type: (Any, Any) -> bool
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


@validate_each('{} !< {}.')
def is_lt(a, b):
    # type: (Any, Any) -> bool
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


@validate_each('{} !> {}.')
def is_gt(a, b):
    # type: (Any, Any) -> bool
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


@validate_each('{} !<= {}.')
def is_lte(a, b):
    # type: (Any, Any) -> bool
    '''
    Validates that a is less than or equal to b.

    Args:
        a (object): Object.
        b (object): Object.

    Raises:
        ValidationError: If a is not less than or equal to b.

    Returns:
        bool: A is less than or equal to b.
    '''
    return a <= b


@validate_each('{} !>= {}.')
def is_gte(a, b):
    # type: (Any, Any) -> bool
    '''
    Validates that a is greater than or equal to b.

    Args:
        a (object): Object.
        b (object): Object.

    Raises:
        ValidationError: If a is not greater than or equal to b.

    Returns:
        bool: A is greater than or equal to b.
    '''
    return a >= b


@validate('{} is not homogenous.')
def is_homogenous(items):
    # type: (List[Any]) -> bool
    '''
    Validates thats all items are equal.

    Args:
        items (list): List of items.

    Raises:
        ValidationError: If items are not all the same.

    Returns:
        bool: Homogeneity of items.
    '''
    if len(items) < 2:
        return True

    first = items[0]
    for item in items[1:]:
        if item != first:
            return False
    return True


@validate_each('{} is not in {}.')
def is_in(a, b):
    # type: (Any, Any) -> bool
    '''
    Validates that each a is in b.

    Args:
        a (object): Object.
        b (object): Object.

    Raises:
        ValidationError: If a is not in b.

    Returns:
        bool: Alls a's in b.
    '''
    return a in b


@validate_each('{} is not an attribute of {}.')
def is_attribute_of(name, object):
    # type: (str, Any) -> bool
    '''
    Validates that each name is an attribute of given object.

    Args:
        a (str): Attribute name.
        b (object): Object.

    Raises:
        ValidationError: If an name is not an attribute of given object.

    Returns:
        bool: Alls names are attributes of object.
    '''
    return hasattr(object, name)


@validate('{} is not a directory or does not exist.')
def is_directory(item):
    # type: (Union[str, Path]) -> bool
    '''
    Validates thats item is a directory.

    Args:
        item (str): Directory path.

    Raises:
        ValidationError: If item is not a directory or does not exist.

    Returns:
        bool: State of item.
    '''
    if not os.path.isdir(item):
        return False
    return True


@validate('{} is not a file or does not exist.')
def is_file(item):
    # type: (Union[str, Path]) -> bool
    '''
    Validates thats item is a file.

    Args:
        item (str): Filepath.

    Raises:
        ValidationError: If item is not a file or does not exist.

    Returns:
        bool: State of item.
    '''
    if not os.path.isfile(item):
        return False
    return True


def is_not_missing_values(items):
    # type: (List[int]) -> bool
    '''
    Validates that sequence of integers is not missing any values.

    Args:
        items (list[int]): Integers.

    Raises:
        ValidationError: If items is missing values.

    Returns:
        bool: State of item.
    '''
    expected = list(range(min(items), max(items) + 1))
    if sorted(items) == expected:
        return True

    diff = sorted(list(set(expected).difference(items)))
    msg = f'Missing values: {diff}.'
    raise ValidationError(msg)


def has_uniform_coordinate_count(items):
    # type: (List[List[int]]) -> bool
    '''
    Validates that non-unique list of coordinates has a uniform count per
    coordinate.

    Args:
        items (list[list[int]]): List of coordinates.

    Raises:
        ValidationError: If coordinate count is non-uniform.

    Returns:
        bool: Uniformity of coordinates.
    '''
    count = Counter(list(map(str, items)))
    if len(set(count.values())) > 1:
        max_ = max(count.values())
        msg = filter(lambda x: x[1] < max_, count.items())  # type: Any
        msg = [eval(x[0]) for x in msg]
        msg = sorted(msg)
        msg = f'Non-uniform coordinate count. Missing coordinates: {msg}.'
        raise ValidationError(msg)
    return True


def has_dense_coordinates(items):
    # type: (List[List[int]]) -> bool
    '''
    Validates that list of coordinates is dense (every point is filled).

    Args:
        items (list[list[int]]): List of coordinates.

    Raises:
        ValidationError: If coordinates are not dense.

    Returns:
        bool: Density of coordinates.
    '''
    # build dense cartesian coordinates
    dense = DataFrame(items) \
        .apply(lambda x: str(list(range(x.min(), x.max() + 1)))) \
        .tolist()
    dense = map(eval, dense)
    dense = map(list, product(*dense))
    dense = list(map(str, dense))

    # find difference between given coords and dense
    coords = list(map(str, items))
    diff = set(dense).difference(coords)  # type: Any
    if len(diff) > 0:
        diff = sorted(list(map(eval, diff)))
        msg = f'Non-dense coordinates. Missing coordinates: {diff}.'
        raise ValidationError(msg)
    return True


def coordinates_begin_at(items, origin):
    # type: (List[List[int]], List[int]) -> bool
    '''
    Validates that the minimum coordinate of a given list equals a given origin.

    Args:
        items (list[list[int]]): List of coordinates.
        origin (list[int]): Origin coordinate.

    Raises:
        ValidationError: If coordinates do not begin at origin.

    Returns:
        bool: State of items.
    '''
    if min(items) == origin:
        return True
    msg = f'Coordinates do not begin at {origin}.'
    raise ValidationError(msg)

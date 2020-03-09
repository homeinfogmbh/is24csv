"""Data parsing functions."""

from datetime import datetime


__all__ = [
    'parse_bool',
    'parse_date',
    'parse_enum',
    'parse_float',
    'parse_int'
]


def parse_bool(string, true='J', false='N', default=None):
    """Derives a boolean value from string if string
    is present or else returns None as not applicable.
    """

    if string == true:
        return True

    if string == false:
        return False

    return default


def parse_date(string, frmt='%d.%m.%Y', default=None):
    """Derives a date value from string if
    string is present or else returns None.
    """

    if string is None:
        return default

    try:
        return datetime.strptime(string, frmt)
    except ValueError:
        return default


def parse_enum(enum, value, preprocess=None, default=None):
    """Parser factory to parse a string,
    for the respective enumeration type.
    """

    if value is None:
        return default

    if preprocess is not None:
        value = preprocess(value)

    try:
        return enum(value)
    except ValueError:
        return default


def parse_float(string, default=None):
    """Fix comma as decimal point and ensure existence
    of some value before actually parsing a float or
    return None if no value is present.
    """

    if string is None:
        return default

    try:
        return float(string.replace(',', '.'))
    except ValueError:
        return default


def parse_int(string, default=None):
    """Ensure existence of some value before parsing
    an integer or return None if no value is present.
    """

    if string is None:
        return default

    try:
        return int(string)
    except ValueError:
        return default

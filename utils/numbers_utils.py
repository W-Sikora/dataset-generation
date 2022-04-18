from numbers import Number

from utils import assertions

ZERO = 0
ONE = 1
TWO = 2


def is_zero(value: Number) -> bool:
    return value == ZERO


def is_one(value: Number) -> bool:
    return value == ONE


def is_even(value: int) -> bool:
    assertions.not_none(value)
    return value % TWO == ZERO


def is_greater_than_zero(value) -> bool:
    assertions.not_none(value)
    return is_greater_than(value, ZERO)


def is_greater_than(value_1, value_2) -> bool:
    assertions.not_none(value_1, value_name = 'value_1')
    assertions.not_none(value_2, value_name = 'value_2')
    return value_1 > value_2


def is_greater_than_or_equal(value_1, value_2) -> bool:
    assertions.not_none(value_1, value_name = 'value_1')
    assertions.not_none(value_2, value_name = 'value_2')
    return value_1 >= value_2


def is_between(value, lower: int, upper: int) -> bool:
    assertions.not_none(value)
    assertions.not_none(lower, value_name = 'lower')
    assertions.not_none(upper, value_name = 'upper')
    return upper > value > lower


def is_between_inclusive(value, lower: int, upper: int) -> bool:
    assertions.not_none(value)
    assertions.not_none(lower, value_name = 'lower')
    assertions.not_none(upper, value_name = 'upper')
    return upper >= value >= lower

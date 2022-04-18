from utils.assertions import has_length

DIVISION = '/'
MINUS = '-'
PLUS = '+'
POWER = '**'
TIMES = '*'
BASIC = [
    DIVISION,
    MINUS,
    PLUS,
    TIMES
]
POSITIVE_AND_NEGATIVE = [
    MINUS,
    PLUS
]


def is_division(value: str) -> bool:
    has_length(value)
    return value == DIVISION


def is_minus(value: str) -> bool:
    has_length(value)
    return value == MINUS


def is_plus(value: str) -> bool:
    has_length(value)
    return value == PLUS


def is_power(value: str) -> bool:
    has_length(value)
    return value == POWER


def is_times(value: str) -> bool:
    has_length(value)
    return value == TIMES

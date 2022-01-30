DIVISION = '/'
TIMES = '*'
MINUS = '-'
PLUS = '+'
POWER = '**'


def is_plus(value: str) -> bool:
    return value == PLUS


def is_minus(value: str) -> bool:
    return value == MINUS


def is_plus_or_minus(value: str) -> bool:
    return is_plus(value) or is_minus(value)



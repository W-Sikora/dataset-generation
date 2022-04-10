ZERO = 0
ONE = 1


def is_zero(value) -> bool:
    return value == ZERO


def is_one(value) -> bool:
    return value == ONE


def is_greater_than_zero(value) -> bool:
    return is_greater_than(value, ZERO)


def is_greater_than(value_1, value_2) -> bool:
    return value_1 > value_2


def is_greater_than_or_equal(value_1, value_2) -> bool:
    return value_1 >= value_2


def is_between(value, lower: int, upper: int) -> bool:
    return upper > value > lower


def is_between_inclusive(value, lower: int, upper: int) -> bool:
    return upper >= value >= lower

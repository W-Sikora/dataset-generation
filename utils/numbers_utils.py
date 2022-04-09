from utils.values import ZERO


def is_greater_than_zero(value) -> bool:
    return is_greater_than(value, ZERO)


def is_greater_than(value_1, value_2) -> bool:
    return value_1 > value_2


def is_between(value, lower: int, upper: int) -> bool:
    return value not in range(lower, upper)

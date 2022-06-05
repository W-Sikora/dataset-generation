from src.utils import assertions

NEAREST_TEN = -1
NEAREST_HUNDRED = -2


def is_between_inclusive(value, lower: int, upper: int) -> bool:
    assertions.not_none(value)
    assertions.not_none(lower, value_name='lower')
    assertions.not_none(upper, value_name='upper')
    return upper >= value >= lower

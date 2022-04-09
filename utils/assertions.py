from utils import string_utils
from utils.messages import NOT_NONE_FAILED_MESSAGE, CONDITION_FAILED_MESSAGE, HAS_LENGTH_FAILED_MESSAGE


def not_none(value, message: str = NOT_NONE_FAILED_MESSAGE):
    if value is None:
        raise ValueError(message)


def is_true(condition: bool, message: str = CONDITION_FAILED_MESSAGE):
    if not condition:
        raise ValueError(message)


def has_length(value: str, message: str = HAS_LENGTH_FAILED_MESSAGE):
    if string_utils.has_length(value):
        raise ValueError(message)

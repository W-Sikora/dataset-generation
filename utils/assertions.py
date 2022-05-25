from typing import List, Tuple
from utils import string_utils
from utils.numbers_utils import is_between_inclusive, ZERO, ONE

NOT_NONE_FAILED_MESSAGE = 'must not be none'
CONDITION_FAILED_MESSAGE = 'condition must not be false'
HAS_LENGTH_FAILED_MESSAGE = 'must not be none or empty'

CONTAINS_ALLOWED_VALUES_FAILED_MESSAGE = 'is outside the allowed values'
PROBABILITY_VALUE_FAILED_MESSAGE = 'must be between 0 and 1 inclusive'
LIST_FAILED_MESSAGE = 'must contain at least one element'
VALUE_NAME_DEFAULT = 'value'
LESS_FIRST_ELEMENT_FAILED_MESSAGE = 'first element of {} must be less than the last'


def not_none(value, value_name: str = VALUE_NAME_DEFAULT, message: str = NOT_NONE_FAILED_MESSAGE):
    if value is None:
        raise ValueError(f'{value_name} {message}')


def is_true(condition: bool, message: str = CONDITION_FAILED_MESSAGE):
    if not condition:
        raise ValueError(message)


def has_length(value: str, value_name: str = VALUE_NAME_DEFAULT, message: str = HAS_LENGTH_FAILED_MESSAGE):
    is_true(string_utils.has_length(value), f'{value_name} {message}')


def is_valid_probability(value, message: str = PROBABILITY_VALUE_FAILED_MESSAGE, value_name: str = VALUE_NAME_DEFAULT):
    if value is None or not is_between_inclusive(value, ZERO, ONE):
        raise ValueError(f'{value_name} {message}')


def not_empty(value: List, message: str = LIST_FAILED_MESSAGE, value_name: str = VALUE_NAME_DEFAULT):
    if not value:
        raise ValueError(f'{value_name} {message}')


def first_element_is_less(value: Tuple,
                          message: str = LESS_FIRST_ELEMENT_FAILED_MESSAGE,
                          value_name: str = VALUE_NAME_DEFAULT):
    if not value[ZERO] < value[-ONE]:
        raise ValueError(message.format(value_name))


def contains(container, value, value_name: str = VALUE_NAME_DEFAULT,
             message: str = CONTAINS_ALLOWED_VALUES_FAILED_MESSAGE):
    if value not in container:
        raise ValueError(f'{value_name} {message}')

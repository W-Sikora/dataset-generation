from src.utils import string_utils
from src.utils.numbers_utils import is_between_inclusive

NOT_NONE_FAILED_MESSAGE = '{} must not be none'
CONDITION_FAILED_MESSAGE = 'condition must not be false'
HAS_LENGTH_FAILED_MESSAGE = '{} must not be none or empty'
PROBABILITY_VALUE_FAILED_MESSAGE = '{} must be between 0 and 1 inclusive'
SIZE_FAILED_MESSAGE = 'size must be an integer greater than 0'
DEFAULT_VALUE_NAME = 'value'
CONTAINER_NAME_DEFAULT = 'container'
DEFAULT_SIZE_NAME = 'size'


def not_none(value,
             value_name: str = DEFAULT_VALUE_NAME,
             message: str = None):
    if value is None:
        if message is None:
            message = NOT_NONE_FAILED_MESSAGE.format(value_name)
        raise ValueError(message)


def is_true(condition: bool,
            message: str = CONDITION_FAILED_MESSAGE):
    not_none(condition, 'condition')
    if not condition:
        raise ValueError(message)


def has_length(value: str,
               value_name: str = DEFAULT_VALUE_NAME,
               message: str = None):
    if message is None:
        message = HAS_LENGTH_FAILED_MESSAGE.format(value_name)
    is_true(string_utils.has_length(value), message)


def is_valid_probability(value,
                         value_name: str = DEFAULT_VALUE_NAME,
                         message: str = None):
    not_none(value, value_name)
    if message is None:
        message = PROBABILITY_VALUE_FAILED_MESSAGE.format(value_name)
    is_true(is_between_inclusive(value, 0, 1), message)


def is_valid_size(value: int,
                  value_name: str = DEFAULT_SIZE_NAME):
    not_none(value, value_name)
    is_true(value > 0, SIZE_FAILED_MESSAGE)


def contains_x_elements(container, number_of_elements: int, container_name: str = CONTAINER_NAME_DEFAULT):
    length = len(container)
    if length != number_of_elements:
        more_or_less = 'more' if length > number_of_elements else 'less'
        raise ValueError(f'{container_name} has {more_or_less} than {number_of_elements} elements')

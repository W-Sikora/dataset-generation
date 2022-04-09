from enum import Enum
from utils.assertions import has_length


class Sign(Enum):
    DIVISION = '/'
    MINUS = '-'
    PLUS = '+'
    POWER = '**'
    TIMES = '*'

    @staticmethod
    def is_division(value: str) -> bool:
        has_length(value)
        return value == Sign.DIVISION.value

    @staticmethod
    def is_minus(value: str) -> bool:
        has_length(value)
        return value == Sign.MINUS.value

    @staticmethod
    def is_plus(value: str) -> bool:
        has_length(value)
        return value == Sign.PLUS.value

    @staticmethod
    def is_power(value: str) -> bool:
        has_length(value)
        return value == Sign.POWER.value

    @staticmethod
    def is_times(value: str) -> bool:
        has_length(value)
        return value == Sign.TIMES.value

    @staticmethod
    def basic() -> set:
        return {
            Sign.DIVISION,
            Sign.MINUS,
            Sign.PLUS,
            Sign.TIMES
        }

    @staticmethod
    def positive_and_negative() -> set:
        return {
            Sign.MINUS,
            Sign.PLUS
        }

    def __str__(self):
        return str(self.value)

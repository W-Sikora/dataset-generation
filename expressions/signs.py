from enum import Enum


class Sign(Enum):
    PLUS = '+'
    MINUS = '-'

    @staticmethod
    def values():
        return [sign.value for sign in Sign]

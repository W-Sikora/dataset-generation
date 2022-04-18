from dataclasses import dataclass

from numpy.random import choice, randint

from expressions.signs import Sign
from util.numbers import ZERO, ONE


@dataclass
class ExpressionGenerator:
    neg_sign_probability: float = 0.5
    coefficient_range: float


    def __generate_sign(self) -> str:
        if ZERO < self.neg_sign_probability > ONE:
            raise ValueError('')
        return choice(Sign.values(), p = [ONE - neg_sign_probability, neg_sign_probability])

    def __generate_coefficient(self, low: int = 2, high: int = 11, negative_sign_probability: float = 0.5) -> str:
        sign = self.generate_sign(negative_sign_probability)
        coefficient = randint(low, high)
        return sign if coefficient == ONE else f'{sign}{coefficient}{TIMES}'
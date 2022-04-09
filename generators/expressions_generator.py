import unittest

from sympy import simplify, Expr
from numpy.random import randint, choice
from numpy import array

from utils.assertions import is_true, not_none
from utils.messages import PROBABILITY_VALUE_FAILED_MESSAGE
from utils.signs import Sign
from utils.numbers_utils import is_between
from utils.values import ZERO, ONE


def generate_sign(negative_sign_probability: float = 0.5) -> str:
    is_true(is_between(negative_sign_probability, ZERO, ONE), PROBABILITY_VALUE_FAILED_MESSAGE)
    return choice(list(Sign.positive_and_negative()), p=[ONE - negative_sign_probability, negative_sign_probability])


def generate_coefficient(low: int = 2, high: int = 11, negative_sign_probability: float = 0.5) -> str:
    sign = generate_sign(negative_sign_probability)
    coefficient = randint(low, high)
    return sign if coefficient == ONE else f'{sign}{coefficient}{Sign.TIMES}'


def generate_single_term(powers: list) -> str:
    if len(powers) <= ONE:
        raise Exception('The power list must have at least one element')
    term = ''
    for i, power in enumerate(powers):

        if power == ONE:
            term += f'x{i + ONE}{Sign.TIMES}'

        elif power > ONE:
            term += f'x{i + ONE}{Sign.POWER}{power}{Sign.TIMES}'

    return term[:-ONE]


if __name__ == '__main__':
    print(generate_single_term())

# def random_powers(number_of_features: int, max_power: int) -> list:
#     count = max_power
#     sum_count = ZERO
#     powers = []
#     for i in range(number_of_features - ONE):
#         random_integer = randint(ZERO, count + ONE)
#         powers.append(random_integer)
#         count -= random_integer
#         sum_count += random_integer
#
#     powers.append(max_power - sum_count)
#
#     return powers
#
#
# def generate_expression(number_of_features: int = 4, number_of_terms: int = 3, max_power: int = 3,
#                         negative_sign_probability: float = 0.3, with_coefficients: bool = True,
#                         min_coefficient: int = 2, max_coefficient: int = 11):
#     min_number_of_features = 2
#     if number_of_features < min_number_of_features:
#         raise Exception(f'The minimum number of features is {min_number_of_features}')
#
#     terms = []
#     for i in range(number_of_terms):
#
#         power_lst = random_powers(number_of_features, max_power)
#         term = generate_single_term(power_lst)
#
#         if with_coefficients:
#             coefficient = generate_coefficient(min_coefficient, max_coefficient, negative_sign_probability)
#             terms.append(f'{coefficient}{term}')
#
#         else:
#             terms.append(term)
#
#     expression = ''.join(term for term in terms)
#
#     return simplify(expression)
#
#
# class TestExpression(unittest.TestCase):
#
#     def test_generate_sign(self):
#         sign = generate_sign()
#
#         self.assertTrue(sign == PLUS or sign == MINUS)
#
#     def test_generate_coefficient(self):
#         coefficient_1 = generate_coefficient(1, 2)
#         coefficient_2 = generate_coefficient(2, 3)
#
#         self.assertTrue(is_plus_or_minus(coefficient_1))
#         self.assertFalse(is_plus_or_minus(coefficient_2))
#
#     def test_generate_single_term(self):
#         single_term_1 = generate_single_term([1, 0, 1])
#         single_term_2 = generate_single_term([1, 2, 3])
#
#         self.assertTrue(single_term_1 == 'x1*x3')
#         self.assertTrue(single_term_2 == 'x1*x2**2*x3**3')

from numbers import Number
from typing import Tuple

from numpy.random import randint, uniform
from sympy import simplify

from utils.assertions import is_true, not_none, first_element_is_less
from utils.numbers_utils import ZERO, ONE, TWO, is_between_inclusive, is_one, is_even
from utils.signs import TIMES, POWER, PLUS
from utils.string_utils import EMPTY_STRING


def generate_polynomial(powers_range: Tuple[Number] = (1, 4),
                        are_powers_integers: bool = True,
                        coefficients_range: Tuple[Number] = (-10, 11),
                        are_coefficients_integers: bool = True,
                        constant_term_present: bool = True,
                        constant_term_range: Tuple[Number] = (-10, 11),
                        is_constant_term_integer: bool = True):
    """
    :return: random polynomial e.g. -4*x**2 + 3*x - 4
    """
    not_none(powers_range, value_name = 'powers_range')
    is_true(len(powers_range) == 2, message = 'powers_range must contain two numbers')
    first_element_is_less(powers_range, value_name = 'powers_range')

    not_none(are_powers_integers, value_name = 'are_powers_integers')
    not_none(coefficients_range, value_name = 'coefficients_range')
    is_true(len(coefficients_range) == 2, message = 'coefficients_range must contain two numbers')
    first_element_is_less(coefficients_range, value_name = 'coefficients_range')

    not_none(are_coefficients_integers, value_name = 'are_coefficients_integers')

    not_none(constant_term_present, value_name = 'constant_term_present')
    not_none(constant_term_range, value_name = 'constant_term_range')
    is_true(len(constant_term_range) == 2, message = 'constant_term_range must contain two numbers')
    first_element_is_less(constant_term_range, value_name = 'constant_term_range')

    not_none(is_constant_term_integer, value_name = 'is_constant_term_integer')

    while True:
        polynomial = __generate_polynomial(powers_range, are_powers_integers, coefficients_range,
                                           are_coefficients_integers, constant_term_present,
                                           constant_term_range, is_constant_term_integer)
        if __is_polynomial_valid(polynomial):
            return polynomial


def __generate_polynomial(powers_range: Tuple[Number],
                          are_powers_integers: bool,
                          coefficients_range: Tuple[Number],
                          are_coefficients_integers: bool,
                          constant_term_present: bool,
                          constant_term_range: Tuple[Number],
                          is_constant_term_integer: bool):
    terms_number = randint(2, 7)

    constant_term = ZERO
    if constant_term_present:
        terms_number -= ONE
        constant_term = __generate_numbers_in_range_without_zero(constant_term_range, ONE, is_constant_term_integer)[
            ZERO]

    powers = __generate_numbers_in_range_without_zero(powers_range, terms_number, are_powers_integers)

    coefficients = __generate_numbers_in_range_without_zero(coefficients_range, terms_number, are_coefficients_integers)

    polynomial = EMPTY_STRING
    for coefficient, power in zip(coefficients, powers):
        polynomial += f'{PLUS}{coefficient}{TIMES}x{POWER}{power}'

    return simplify(f'{polynomial}{PLUS}{constant_term}')


def generate_multivariate_polynomial():
    pass


def __generate_numbers_in_range_without_zero(value_range: Tuple[Number], size: int, are_integers: bool):
    function = randint if are_integers else uniform
    if is_between_inclusive(ZERO, value_range[ZERO], value_range[-ONE]):
        if is_one(size):
            return function(value_range[ZERO], ZERO, ONE)
        if is_even(size):
            first_part = function(value_range[ZERO], ZERO, int(size / TWO))
            second_part = function(ZERO, value_range[-ONE], int(size / TWO))
        else:
            first_part_size = int((size - ONE) / TWO)
            first_part = function(value_range[ZERO], ZERO, first_part_size)
            second_part_size = size - first_part_size
            second_part = function(ZERO, value_range[-ONE], second_part_size)
        return [*first_part, *second_part]
    else:
        return function(value_range[ZERO], value_range[-ONE], size)


def __is_polynomial_valid(polynomial) -> bool:
    return not isinstance(polynomial, Number) or 'x' in polynomial

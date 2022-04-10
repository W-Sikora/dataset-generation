from numpy.random import randint, choice
from typing import List

from sympy import simplify

from utils import assertions
from utils.signs import Sign
from utils.numbers_utils import ONE, is_one


def __generate_sign(negative_sign_probability: float = 0.5) -> str:
    probabilities = (ONE - negative_sign_probability, negative_sign_probability)
    return choice(Sign.positive_and_negative_as_list(), p=probabilities)


def generate_coefficient(low: int = 2, high: int = 11, negative_sign_probability: float = 0.5) -> str:
    assertions.not_none(low, value_name='low')
    assertions.not_none(high, value_name='high')
    assertions.is_valid_probability(negative_sign_probability, value_name='negative sign probability')

    sign = __generate_sign(negative_sign_probability)
    coefficient = randint(low, high)
    if is_one(coefficient):
        return sign
    return f'{sign}{coefficient}{Sign.TIMES}'


def generate_single_term(powers: List[int]) -> str:
    if len(powers) <= ONE:
        raise Exception('The power list must have at least one element')
    term = ''
    for i, power in enumerate(powers):

        if power == ONE:
            term += f'x{i + ONE}{Sign.TIMES}'

        elif power > ONE:
            term += f'x{i + ONE}{Sign.POWER}{power}{Sign.TIMES}'

    return term[:-ONE]


def random_powers(number_of_features: int, max_power: int) -> list:
    count = max_power
    sum_count = ZERO
    powers = []
    for i in range(number_of_features - ONE):
        random_integer = randint(ZERO, count + ONE)
        powers.append(random_integer)
        count -= random_integer
        sum_count += random_integer

    powers.append(max_power - sum_count)

    return powers


def generate_expression(number_of_features: int = 4, number_of_terms: int = 3, max_power: int = 3,
                        negative_sign_probability: float = 0.3, with_coefficients: bool = True,
                        min_coefficient: int = 2, max_coefficient: int = 11):
    min_number_of_features = 2
    if number_of_features < min_number_of_features:
        raise Exception(f'The minimum number of features is {min_number_of_features}')

    terms = []
    for i in range(number_of_terms):

        power_lst = random_powers(number_of_features, max_power)
        term = generate_single_term(power_lst)

        if with_coefficients:
            coefficient = generate_coefficient(min_coefficient, max_coefficient, negative_sign_probability)
            terms.append(f'{coefficient}{term}')

        else:
            terms.append(term)

    expression = ''.join(term for term in terms)

    return simplify(expression)


if __name__ == '__main__':
    print(generate_single_term())

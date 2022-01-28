from numpy.random import randint, choice

PLUS = '+'
MINUS = '-'
SIGNS = [PLUS, MINUS]
ZERO = 0
ONE = 1


def __generate_coefficient(low: int = 2, high: int = 11, negative_sign_probability: float = 0.5) -> str:
    sign = choice(SIGNS, p=[ONE - negative_sign_probability, negative_sign_probability])
    coefficient = randint(low, high)
    return sign if coefficient == ONE else f' {sign} {coefficient}*'


def __generate_single_term(powers: list) -> str:
    term = ''
    for i, power in enumerate(powers):
        if power == 1:
            term += f'x{i + ONE}*'
        elif power > 1:
            term += f'x{i + ONE}**{power}*'
    return term[:-ONE]


def __random_powers(number_of_features: int, max_power: int) -> list:
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


def generate_expression(number_of_features: int = 5, max_power: int = 3, negative_sign_probability: float = 0.3,
                        with_coefficients: bool = True, number_of_terms: int = 3,
                        min_coefficient: int = 2, max_coefficient: int = 11):
    min_number_of_features = 2
    if number_of_features < min_number_of_features:
        raise Exception(f'The minimum number of features is {min_number_of_features}')

    if negative_sign_probability > ONE or negative_sign_probability < ZERO:
        raise Exception('The probability must be between 0 and 1')

    expression = ''
    terms = []

    for i in range(number_of_terms):
        power_lst = __random_powers(number_of_features, max_power)
        term = __generate_single_term(power_lst)
        if with_coefficients:
            coefficient = __generate_coefficient(min_coefficient, max_coefficient, negative_sign_probability)
            terms.append(f'{coefficient}{term}')
        else:
            terms.append(term)

    for term in terms:
        expression += f'{term}'

    expression = expression.strip()

    return expression[ONE:] if expression.startswith(PLUS) else expression

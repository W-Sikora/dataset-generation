from typing import List

import numpy.random as rnd

import src.utils.assertions as assertions


def generate_binary_features(size: int, name: str, options: List[str], probability: float):
    assertions.has_length(name, 'name')
    assertions.contains_x_elements(options, 2, 'options')
    assertions.is_valid_probability(probability, f'probability of {name}')

    return rnd.choice(a=options, size=size, p=[probability, 1 - probability])


def generate_categorical_features(size: int,
                                  options: List[str],
                                  probabilities: List[float]):
    assertions.is_valid_size(size)

    assertions.not_none(options, 'options')
    assertions.not_none(probabilities, 'probabilities')

    options_length, probabilities_length = len(options), len(probabilities)
    assertions.is_true(options_length > 0, 'options size must be greater than 0')
    assertions.is_true(len(set(options)) == options_length, 'options must be unique')

    assertions.is_true(options_length == probabilities_length, 'size of options and probabilities must be equal')

    probabilities_sum = 0
    for probability in probabilities:
        assertions.is_valid_probability(probability, 'probability')
        probabilities_sum += probability
    assertions.is_true(probabilities_sum == 1, 'probabilities must sum to one')

    return rnd.choice(a=options,
                      size=size,
                      p=probabilities)

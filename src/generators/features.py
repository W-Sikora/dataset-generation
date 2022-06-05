from typing import List

import numpy.random as rnd

import src.utils.assertions as assertions


def generate_binary_features(size: int, name: str, options: List[str], probability: float):
    assertions.has_length(name, 'name')
    assertions.contains_x_elements(options, 2, 'options')
    assertions.is_valid_probability(probability, f'probability of {name}')

    return rnd.choice(a=options, size=size, p=[probability, 1 - probability])

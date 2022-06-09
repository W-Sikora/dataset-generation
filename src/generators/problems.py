from typing import Callable, Union

from numpy import ndarray
from pandas import DataFrame, concat

import src.utils.assertions as assertions
from src.utils.string_utils import is_string


def generate_regression_problem(features: DataFrame,
                                target_function: Union[str, Callable],
                                output_name: str,
                                noise: ndarray = None,
                                shuffle: bool = True):
    assertions.not_none(features, 'features')
    assertions.not_none(target_function, 'target function')
    assertions.has_length(output_name, 'output name')
    assertions.not_none(shuffle, 'shuffle')

    return __generate_problem(features, target_function, output_name, noise, shuffle)


def generate_classification_problem(features: DataFrame,
                                    target_function: Union[str, Callable],
                                    output_name: str,
                                    assignment_function: Callable,
                                    noise: ndarray = None,
                                    shuffle: bool = True):
    assertions.not_none(features, 'features')
    assertions.not_none(target_function, 'target function')
    assertions.has_length(output_name, 'output name')
    assertions.not_none(assignment_function, 'assignment function')
    assertions.not_none(shuffle, 'shuffle')

    features, outputs = __generate_problem(features, target_function, output_name, noise, shuffle)
    outputs = outputs.apply(assignment_function).astype('category')

    return features, outputs


def __generate_problem(features: DataFrame,
                       target_function: Union[str, Callable],
                       output_name: str,
                       noise: ndarray = None,
                       shuffle: bool = True):
    if is_string(target_function):
        outputs = features.eval(target_function).iloc[:, -1]
    else:
        outputs = target_function(features)
    outputs = outputs.rename(output_name)

    if noise is not None:
        outputs += noise

    if shuffle:
        data = [features, outputs]
        framed_data = concat(data, axis=1)
        shuffle_data = framed_data.sample(frac=1).reset_index(drop=True)
        outputs = shuffle_data.iloc[:, -1]
        features = shuffle_data.drop(outputs.name, axis=1)

    return features, outputs

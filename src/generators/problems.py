from typing import Callable

from pandas import DataFrame, concat

import src.utils.assertions as assertions


def generate_regression_problem(features: DataFrame, target_function: str, noise: DataFrame = None,
                                shuffle: bool = True):
    """
    :param features:
    :param target_function:
    :param noise:
    :param shuffle:
    :return:
    """
    return __generate_problem(features, target_function, noise, shuffle)


def generate_classification_problem(features: DataFrame, target_function: str, assignment_function: Callable,
                                    noise: DataFrame = None, shuffle: bool = True):
    """
    :param features:
    :param target_function:
    :param assignment_function:
    :param noise:
    :param shuffle:
    :return:
    """
    features, outputs = __generate_problem(features, target_function, noise, shuffle)
    outputs = outputs.apply(assignment_function).astype('category')

    return features, outputs


def __generate_problem(features: DataFrame, target_function: str, noise: DataFrame = None,
                       shuffle: bool = True):
    """
    :param features:
    :param target_function:
    :param noise:
    :param shuffle:
    """
    assertions.has_length(target_function)

    outputs = features.eval(target_function).iloc[:, -1]

    if noise is not None:
        outputs += noise

    if shuffle:
        data = [features, outputs]
        framed_data = concat(data, axis=1)
        shuffle_data = framed_data.sample(frac=1).reset_index(drop=True)
        outputs = shuffle_data.iloc[:, -1]
        features = shuffle_data.drop(outputs.name, axis=1)

    return features, outputs

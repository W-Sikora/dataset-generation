from pandas import DataFrame

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
    return __generate_problem(features, target_function, noise, shuffle, True)


def generate_classification_problem(features: DataFrame, target_function: str, noise: DataFrame = None,
                                    shuffle: bool = True):
    """
    :param features:
    :param target_function:
    :param noise:
    :param shuffle:
    :return:
    """
    outputs = __generate_problem(features, target_function, noise, shuffle, False)

    return features, outputs


def __generate_problem(features: DataFrame, target_function: str, noise: DataFrame = None,
                       shuffle: bool = True, return_features: bool = True):
    """
    :param features:
    :param target_function:
    :param noise:
    :param shuffle:
    :param return_features:
    :return:
    """
    assertions.has_length(target_function)

    outputs = features.eval(target_function).iloc[:, -1]

    if noise is not None:
        outputs += noise

    if shuffle:
        features = features.sample(frac=1).reset_index(drop=True)
        outputs = outputs.sample(frac=1).reset_index(drop=True)

    return features, outputs if return_features else outputs

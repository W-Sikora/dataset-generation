from pandas import DataFrame

import utils.assertions as assertions


def generate_regression_problem(features: DataFrame, target_function: str, noise: DataFrame = None,
                                shuffle: bool = True):
    """
    :param features:
    :param target_function:
    :param noise:
    :param shuffle:
    :return:
    """
    assertions.has_length(target_function)

    outputs = features.eval(target_function).iloc[:, -1]

    if noise is not None:
        outputs += noise

    if shuffle:
        features = features.sample(frac=1).reset_index(drop=True)
        outputs = outputs.sample(frac=1).reset_index(drop=True)

    return features, outputs

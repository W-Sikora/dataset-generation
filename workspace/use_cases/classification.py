# def generate_binary_classification_problem(features: DataFrame, target_function: str,
#                                            make_harder: bool = False, p: float = 0,
#                                            seed=None, shuffle: bool = True) -> Tuple[DataFrame, DataFrame]:
#     outputs = features.eval(target_function).iloc[:, -1]
#     outputs = outputs.apply(lambda value: 1 if value > 0 else 0)
#
#     if make_harder:
#         if seed is not None:
#             rnd.default_rng(seed)
#         binary_values = rnd.choice([0, 1], size=outputs.size, p=[p, 1 - p])
#         outputs = DataFrame(np.logical_xor(outputs, binary_values), dtype=int)
#     else:
#         outputs = DataFrame(outputs, dtype=int)
#
#     if shuffle:
#         features = features.sample(frac=1).reset_index(drop=True)
#         outputs = outputs.sample(frac=1).reset_index(drop=True)
#
#     return features, outputs
#
# size = 100
# features = DataFrame({
#     'x1': rnd.random(size),
#     'x2': rnd.lognormal(mean=1, sigma=0.5, size=size)
# })
# inp, out = generate_binary_classification_problem(features, 'y = x2 - 10', make_harder=False, p=0.82)
#

# from datasets.util.dictionary_utils import keys_to_list
# from datasets.util.rounding_mode import NEAREST_TEN, NEAREST_HUNDRED
#
# MIN_COOKING_TIME = 240
# MAX_COOKING_TIME = 1140
#
# MIN_AMOUNT_OF_WATER = 90
# MAX_AMOUNT_OF_WATER = 6200
#
# MIN_AMOUNT_OF_PASTA = 50
# MAX_AMOUNT_OF_PASTA = 500
#
# PASTA = {
#     'Farfalle': 780,
#     'Fusilli': 660,
#     'Penne': 600,
#     'Rigatoni': 720,
#     'Spaghetti': 480,
#     'Tagliatelle': 360
# }
#
# SALTED = {
#     'salted': 1,
#     'unsalted': 0
# }
#
# STIRRED = {
#     'stirred': 1,
#     'unstirred': 0
# }
#
# COVERED = {
#     'covered': 1,
#     'uncovered': 0
# }
#
# DEGREE_OF_DONENESS = [
#     'undercooked',
#     'al dente',
#     'overcooked'
# ]
#
# THRESHOLD = 35
#
#
# def calculate_score(pasta):
#     optimum_cooking_time_for_pasta = p
#
# def get_dataset(size: int, f=None) -> DataFrame:
#     """
#     :param f:
#     :param size:
#     :return: DataFrame (synthetic type; cook time; amount of water, amount of synthetic; salted; stirred; )
#     """
#
#     def calculate_score(measurements: dict, index: int, f=None) -> float:
#         """
#         :param f:
#         :param measurements:
#         :param index:
#         :return:
#         """
#         pasta_type = measurements['pasta type'][index]
#         cook_time = measurements['cook time'][index]
#         amount_of_water = measurements['amount of water'][index]
#         amount_of_pasta = measurements['amount of pasta'][index]
#         salted = SALTED[measurements['salted'][index]]
#         stirred = STIRRED[measurements['stirred'][index]]
#         covered = COVERED[measurements['covered'][index]]
#
#         proper_cook_time = PASTA[pasta_type]
#
#         if f is not None:
#             return f(measurements, index)
#
#         return 1 + (covered / 3 + stirred / 8 + salted / 21) * amount_of_water / (10 * amount_of_pasta) * (
#                 cook_time - proper_cook_time)
#
#     def assign_to_category(score: float) -> str:
#         """
#         :param score:
#         :return:
#         """
#         if score < - THRESHOLD:
#             return DEGREE_OF_DONENESS[0]
#         elif score <= THRESHOLD:
#             return DEGREE_OF_DONENESS[1]
#         else:
#             return DEGREE_OF_DONENESS[2]
#
#     assert size > 0, 'Size of the dataset must be greater than 0'
#
#     data = {
#         'pasta type': choice(keys_to_list(PASTA), size),
#         'cook time': randint(MIN_COOKING_TIME, MAX_COOKING_TIME, size),
#         'amount of water': round(randint(MIN_AMOUNT_OF_WATER, MAX_AMOUNT_OF_WATER, size), NEAREST_HUNDRED),
#         'amount of pasta': round(randint(MIN_AMOUNT_OF_PASTA, MAX_AMOUNT_OF_PASTA, size), NEAREST_TEN),
#         'salted': choice(keys_to_list(SALTED), size),
#         'stirred': choice(keys_to_list(STIRRED), size),
#         'covered': choice(keys_to_list(COVERED), size)
#     }
#
#     scores = [calculate_score(data, index, f) for index in range(size)]
#
#     data['doneness'] = [assign_to_category(score) for score in scores]
#
#     return DataFrame(data)

import numpy.random as rnd
from pandas import DataFrame

from src import generate_binary_features
from src.utils.numbers_utils import NEAREST_HUNDRED, NEAREST_TEN

SALTED_OPTIONS = ['salted', 'unsalted']
STIRRED_OPTIONS = ['stirred', 'unstirred']
COVERED_OPTIONS = ['covered', 'uncovered']
PASTA_OPTIONS = ['Farfalle', 'Fusilli', 'Penne', 'Rigatoni', 'Spaghetti', 'Tagliatelle']
DEGREE_OF_DONENESS = ['undercooked', 'al dente', 'overcooked']

SALTED_FEATURE_NAME = SALTED_OPTIONS[0]
STIRRED_FEATURE_NAME = STIRRED_OPTIONS[0]
COVERED_FEATURE_NAME = COVERED_OPTIONS[0]
PASTA_FEATURE_NAME = 'pasta'
COOK_TIME_FEATURE_NAME = 'cook time'
AMOUNT_OF_PASTA_FEATURE_NAME = 'amount of pasta'
AMOUNT_OF_WATER_FEATURE_NAME = 'amount of water'






SIZE = 100

features = DataFrame()

salted_probability = 0.6
features[SALTED_FEATURE_NAME] = generate_binary_features(SIZE, SALTED_FEATURE_NAME, SALTED_OPTIONS, salted_probability)

stirred_probability = 0.7
features[STIRRED_FEATURE_NAME] = generate_binary_features(SIZE, STIRRED_FEATURE_NAME, STIRRED_OPTIONS,
                                                          stirred_probability)

covered_probability = 0.5
features[COVERED_FEATURE_NAME] = generate_binary_features(SIZE, COVERED_FEATURE_NAME, COVERED_OPTIONS,
                                                          covered_probability)

pasta_probability = [0.11, 0.29, 0.17, 0.13, 0.15, 0.15]
features[PASTA_FEATURE_NAME] = rnd.choice(a=PASTA_OPTIONS, size=SIZE, p=pasta_probability)

features[COOK_TIME_FEATURE_NAME] = rnd.randint(low=350, high=1000, size=SIZE)

features[AMOUNT_OF_PASTA_FEATURE_NAME] = rnd.normal(loc=500, scale=80, size=SIZE)
features[AMOUNT_OF_PASTA_FEATURE_NAME] = features[AMOUNT_OF_PASTA_FEATURE_NAME].apply(
    lambda value: round(value, NEAREST_TEN))

features[AMOUNT_OF_WATER_FEATURE_NAME] = features[AMOUNT_OF_PASTA_FEATURE_NAME].apply(
    lambda value: value * rnd.randint(5, 15))
features[AMOUNT_OF_WATER_FEATURE_NAME] = features[AMOUNT_OF_WATER_FEATURE_NAME].apply(
    lambda value: round(value, NEAREST_HUNDRED))

target_function = f'1/10 - \'{AMOUNT_OF_PASTA_FEATURE_NAME}\' / \'{AMOUNT_OF_WATER_FEATURE_NAME}\''

# features, outputs = generate_pasta_classification_problem(features, target_function)

print(outputs)
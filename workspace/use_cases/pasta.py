import numpy.random as rnd
from pandas import DataFrame

from src import generate_categorical_features, generate_classification_problem
from src.utils.numbers_utils import NEAREST_HUNDRED, NEAREST_TEN

SIZE = 10000
SEED = 2
rnd.seed(SEED)

SALTED_OPTIONS = [
    'salted',
    'unsalted'
]

STIRRED_OPTIONS = [
    'stirred',
    'unstirred'
]

COVERED_OPTIONS = [
    'covered',
    'uncovered'
]

PASTA_OPTIONS = [
    'Farfalle',
    'Penne',
    'Rigatoni',
    'Spaghetti',
    'Tagliatelle',
]

features = DataFrame()

salted_probability = 0.60
features['salted'] = generate_categorical_features(SIZE, SALTED_OPTIONS,
                                                   [salted_probability, 1 - salted_probability])

stirred_probability = 0.50
features['stirred'] = generate_categorical_features(SIZE, STIRRED_OPTIONS,
                                                    [stirred_probability, 1 - stirred_probability])

covered_probability = 0.40
features['covered'] = generate_categorical_features(SIZE, COVERED_OPTIONS,
                                                    [covered_probability, 1 - covered_probability])

pastas_probabilities = [0.18, 0.19, 0.22, 0.22, 0.19]
features['pasta'] = generate_categorical_features(SIZE, PASTA_OPTIONS,
                                                  pastas_probabilities)

features['cook time'] = rnd.randint(low=360, high=800, size=SIZE)
features['cook time'] = features['cook time'].apply(lambda val: round(val, NEAREST_TEN))

features['pasta amount'] = rnd.normal(loc=500, scale=50, size=SIZE)
features['pasta amount'] = features['pasta amount'].apply(lambda val: round(val, NEAREST_TEN)).astype(int)

features['water amount'] = features['pasta amount'].apply(
    lambda val: round(val * rnd.randint(7, 13), NEAREST_HUNDRED))


def calculate_score(dataset: DataFrame):
    def get_proper_cooking_time(pasta: str):
        if pasta == 'Farfalle':
            return 780
        elif pasta == 'Penne':
            return 600
        elif pasta == 'Rigatoni':
            return 720
        elif pasta == 'Spaghetti':
            return 480
        elif pasta == 'Tagliatelle':
            return 360
        return -1

    pasta_type = dataset['pasta']
    water_amount = dataset['water amount']
    pasta_amount = dataset['pasta amount']
    cook_time = dataset['cook time']
    salted = dataset['salted'] == 'salted'
    stirred = dataset['stirred'] == 'stirred'
    covered = dataset['covered'] == 'covered'

    proper_cooking_time = pasta_type.apply(lambda pasta: get_proper_cooking_time(pasta))

    cook_time = cook_time.loc[salted] = cook_time * 1.01
    cook_time = cook_time.loc[stirred] = cook_time * 1.05
    cook_time = cook_time.loc[covered] = cook_time * 1.23

    return (water_amount / pasta_amount - 10) + (cook_time / proper_cooking_time - 1)


def assign_label(score):
    threshold = 0.15
    if score < - threshold:
        return 'undercooked'
    elif threshold >= score >= -threshold:
        return 'al dente'
    else:
        return 'overcooked'


noise = rnd.normal(0, 0.2, SIZE)

inputs, outputs = generate_classification_problem(features, calculate_score,
                                                  output_name='degrees of doneness',
                                                  assignment_function=assign_label,
                                                  noise=noise)
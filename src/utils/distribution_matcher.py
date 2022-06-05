from fitter import Fitter, get_common_distributions, get_distributions
from numpy import array

DISCRETE_DISTRIBUTIONS = [
    'poisson',
    'betabinom',
    'binom',
    'boltzmann',
    'planck',

]


def match_distribution(data):
    fitter = Fitter(data)
    fitter.fit()
    return fitter.get_best()

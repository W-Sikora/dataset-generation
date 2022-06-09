from fitter import Fitter

DISCRETE_DISTRIBUTIONS = [

]


def match_distribution(data):
    fitter = Fitter(data)
    fitter.fit()
    return fitter.get_best()

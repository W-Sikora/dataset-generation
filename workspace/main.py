import numpy.random as rnd
from pandas import DataFrame

from src import generate_classification_problem

SIZE = 100

x = DataFrame({
    'x1': rnd.normal(12, 3, SIZE),
    'x2': rnd.random(SIZE),
    'x3': rnd.uniform(-10, 0, SIZE)
})


def assignment_function(value):
    if value < -5:
        return -1
    elif -30 >= value >= 30:
        return 0
    else:
        return 1


inp, out = generate_classification_problem(x, 'y = x1/2 * x2 + 3*x3', assignment_function)

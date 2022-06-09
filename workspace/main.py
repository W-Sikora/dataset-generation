import numpy.random as rnd
from pandas import DataFrame

from src import generate_classification_problem, load_apartments

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

import numpy as np

inp, out = generate_classification_problem(x, 'y = x1/2 * x2 + 3*x3', assignment_function)

apartments = load_apartments()
apartments['Year'] = apartments['Date'].values.astype(np.int64)
print(apartments)
print(apartments.isna().sum().sum())

rooms = apartments['Rooms']
area = apartments['Area']
import matplotlib.pyplot as plt

# plt.plot(rooms, area, '.')
# plt.show()

import seaborn as sns

corrMatrix = apartments.corr()
color_palette = sns.color_palette("Blues", as_cmap=True)
sns.heatmap(corrMatrix, annot=True, square=True, cmap=color_palette)
g = sns.PairGrid(apartments)
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
plt.show()
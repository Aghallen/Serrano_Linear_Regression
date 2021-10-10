# Based on:
# Linear Regression: A friendly introduction by Luis Serrano.
# https://www.youtube.com/watch?v=wYPUhge9w5c

from cost import Cost
from data_creator import DataCreator
import numpy as np
from least_square_method import LeastSquareMethod
from linear import Linear
from nudger import *
from timing import Timing

x_start=0
x_stop=100
x_count = x_stop - x_start + 1
x_values = [int(x) for x in np.linspace(x_start, x_stop, x_count)]

data_creator = DataCreator(x_values, slope=2, intercept=5)
data_creator.add_noise(dependent=30, independent=5, seed=42)
X, y = data_creator.batch()

# import matplotlib.pyplot as plt;plt.scatter(X, y);plt.show()

LeastSquareMethod().show(X, y)
print()

# Calculate initial values.
slope, intercept = Linear().parameters(X, y)
print(f'Initial parameters.\nslope: {slope:.1f} intercept: {intercept:.1f}\n')


lowest_cost = float('inf')
best_slope = slope
best_intercept = intercept

learning_rate = 1
outer_range = 5
inner_range = 1000
for outer_loop in range(outer_range):
    for loop in range(inner_range):
        rnd_index = np.random.randint(0, x_count)

        rnd_x = x_values[rnd_index]
        y_pred = slope * rnd_x + intercept
        y_obs = y[rnd_index]

        slope_factor, intercept_factor = Nudger().nudge(rnd_x, y_obs, y_pred)
        slope += slope_factor * learning_rate
        intercept += intercept_factor * learning_rate

        dummy, y_new = DataCreator(x_values, slope, intercept).batch()
        cost = Cost.rmse(y, y_new)
        if cost < lowest_cost:
            lowest_cost = cost
            best_slope = slope
            best_intercept = intercept
            print(f'Iteration: {outer_loop * 1000 + loop} slope: {slope:.1f} intercept: {intercept:.1f} cost: {cost:.2f}')
            slope = best_slope
            intercept = best_intercept

    learning_rate *= 0.1

exit()
dummy, y_predicted = DataCreator(x_values, best_slope, best_intercept).batch()
filename = 'xy.txt'  # Located in the same directory as the current file.
import pathlib
full_filename = str(pathlib.Path().absolute().joinpath('xy.txt'))
with open(full_filename, 'w') as f:
    for obs, pred in zip(y, y_predicted):
        f.write(f'{obs:.1f} {pred:.2f}\n')


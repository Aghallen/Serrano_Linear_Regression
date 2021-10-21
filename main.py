# Based on:
# Linear Regression: A friendly introduction by Luis Serrano.
# https://www.youtube.com/watch?v=wYPUhge9w5c
from scipy import stats
from cost import Cost
from data_creator import DataCreator
import numpy as np
from least_square_method import LeastSquareMethod
from linear import Linear
from nudger import *
from timing import Timing
from plotter import *
import matplotlib.pyplot as plt
from line import *

x_start = 0; x_stop = 200; x_count = x_stop - x_start + 1
x_values = [int(x) for x in np.linspace(x_start, x_stop, x_count)]

data_creator = DataCreator(x_values, slope=1, intercept=5)
data_creator.add_noise(dependent=50, independent=50, seed=42)
X, y = data_creator.batch()


slope_lsm, intercept_lsm, r, p, std_err = stats.linregress(X, y)
print(slope_lsm, intercept_lsm)

line = Line().create_by_slope_intercept(slope_lsm, intercept_lsm)
print(line.slope, line.intercept)

plot_xmin = -75; plot_xmax = 275; plot_ymin = -75; plot_ymax = 375
plotter = Plotter(xmin=plot_xmin, xmax=plot_xmax, ymin=plot_ymin, ymax=plot_ymax)
plotter.set_step(step=100, step_minor=50)
plotter.scatter(X, y)
x1, y1, x2, y2 = line.clip_line(plot_xmin, plot_xmax, plot_ymin, plot_ymax)
print(x1, y1, x2, y2)
plotter.draw_line(x1, y1, x2, y2)

line2 = Line().create_by_slope_intercept(1, 100)
x1, y1, x2, y2 = line2.clip_line(plot_xmin, plot_xmax, plot_ymin, plot_ymax)
print(x1, y1, x2, y2)
plotter.draw_line(x1, y1, x2, y2, color='green')


plotter.show()
exit()



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


plotter = Plotter(-100, 100, -100, 100)
plt.scatter(X, y)
plotter.show()
exit()


exit()
dummy, y_predicted = DataCreator(x_values, best_slope, best_intercept).batch()
filename = 'xy.txt'  # Located in the same directory as the current file.
import pathlib
full_filename = str(pathlib.Path().absolute().joinpath('xy.txt'))
with open(full_filename, 'w') as f:
    for obs, pred in zip(y, y_predicted):
        f.write(f'{obs:.1f} {pred:.2f}\n')


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
from window import *


def create_data(x_start, x_stop, x_count):
    x_values = [int(x) for x in np.linspace(x_start, x_stop, x_count)]
    data_creator = DataCreator(x_values, slope=1, intercept=5)
    data_creator.add_noise(dependent=50, independent=50, seed=42)
    X, y = data_creator.batch()
    return X, y

def create_lsm_line(X, y):
    slope_lsm, intercept_lsm, r, p, std_err = stats.linregress(X, y)
    print(f'slope_lsm: {slope_lsm:.1f} intercept_lsm: {intercept_lsm:.1f}')
    lsm_line = Line().create_by_slope_intercept(slope_lsm, intercept_lsm)
    return lsm_line

def update(cost, slope, intercept, current_line):
    lowest_cost = cost
    best_slope = slope
    best_intercept = intercept

    line = Line().create_by_slope_intercept(slope, intercept)
    x1, y1, x2, y2 = line.clip_line(plot_window)
    current_line.remove()
    current_line = plotter.draw_line(x1, y1, x2, y2, color='red')

    plt.pause(1)

    return lowest_cost, best_slope, best_intercept, current_line

def prepare_plotting():
    plotter = Plotter(plot_window)
    plotter.set_spine_and_grid(ticks_step_major=100, ticks_step_minor=10, grid_alpha=0.05, spine_alpha=0.60)
    plotter.prepare_plotting()

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.tight_layout()

    return plotter

def nudge(intercept, learning_rate, slope, x_count):
    # Pick random x and its corresponding observed and predicted values.
    index = np.random.randint(0, x_count)
    x = X[index]
    y_obs = y[index]
    y_pred = slope * x + intercept

    # Nudge towards new slope and intercept.
    slope_factor, intercept_factor = Nudger().nudge(x, y_obs, y_pred)
    slope += slope_factor * learning_rate
    intercept += intercept_factor * learning_rate

    return intercept, slope

def main(slope, intercept, current_line):
    lowest_cost = float('inf'); learning_rate = 1; outer_range = 100; inner_range = 1000
    for outer_loop in range(outer_range):
        for loop in range(inner_range):
            intercept, slope = nudge(intercept, learning_rate, slope, x_count)

            dummy, y_new = DataCreator(X, slope, intercept).batch()
            cost = Cost.rmse(y, y_new)
            # print(f'cost: {cost}')
            if cost < lowest_cost:
                lowest_cost, best_slope, best_intercept, current_line = update(cost, slope, intercept, current_line)
                print(f'Iteration: {outer_loop * 1000 + loop} slope: {slope:.1f} intercept: {intercept:.1f} cost: {cost:.2f}')

        learning_rate *= 0.95


def show_init():
    plotter.scatter(X, y)
    # Show reference line using Least Square Method.
    lsm_line = create_lsm_line(X, y)
    x1, y1, x2, y2 = lsm_line.clip_line(plot_window)
    plotter.draw_line(x1, y1, x2, y2, color='blue', alpha=0.5)
    LeastSquareMethod().show(X, y)
    print()


def prepare_regression():

    # Calculate initial values.
    # slope, intercept = Linear().parameters(X, y)
    slope, intercept = 0, -25
    line = Line().create_by_slope_intercept(slope, intercept)
    x1, y1, x2, y2 = line.clip_line(plot_window)
    current_line = plotter.draw_line(x1, y1, x2, y2, color='red')
    plt.pause(1)
    print(f'Initial parameters.\nslope: {slope:.1f} intercept: {intercept:.1f}\n')
    return slope, intercept, current_line


if __name__ == '__main__':
    x_start = 0; x_stop = 200; x_count = x_stop - x_start + 1
    plot_window = Window(xmin=-75, xmax=275, ymin=-75, ymax=375)
    plotter = prepare_plotting()
    X, y = create_data(x_start, x_stop, x_count)

    show_init()
    slope, intercept, current_line = prepare_regression()
    main(slope, intercept, current_line)

    input('Press any key to exit...')


import matplotlib.pyplot as plt
# from my_data_classes import *
from polyplot_ax import PyplotAx
import matplotlib.patches as patches


class Plotter():
    def __init__(self, plot_window):
        self.plot_window = plot_window
        self.pyplot_ax = PyplotAx(self.plot_window.xmin,
                                  self.plot_window.xmax,
                                  self.plot_window.ymin,
                                  self.plot_window.ymax)


    def set_spine_and_grid(self, ticks_step_major, ticks_step_minor, grid_alpha=0.05, spine_alpha=0.40):
        self.pyplot_ax.set_spine_and_grid(ticks_step_major, ticks_step_minor, grid_alpha, spine_alpha)

    def prepare_plotting(self):
        self.ax = self.pyplot_ax.ax()

    def draw_box(self, box, color='k'):
        llc, w, h = box.border_definition()
        rect = patches.Rectangle(llc, w, h, linewidth=.3, edgecolor=color, facecolor='none')
        self.ax.add_patch(rect)

    def draw_line(self, x1, y1, x2, y2,  color='black', alpha=0.5):
        xs = [x1, x2]
        ys = [y1, y2]
        ln, = plt.plot(xs, ys, color=color, linewidth=1, alpha=alpha)
        return ln

    def scatter(self, xs, ys, color='k'):
        plt.scatter(xs, ys, s=1, c=color)

    def clear_all(self):
        for artist in plt.gca().lines + plt.gca().collections:
            artist.remove()

    def clear(self):
        for artist in plt.gca().lines:
            artist.remove()

    def show(self):
        plt.subplots_adjust(wspace=0, hspace=0)
        plt.tight_layout()
        plt.show()
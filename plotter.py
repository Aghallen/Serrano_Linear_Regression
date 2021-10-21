import matplotlib.pyplot as plt

from polyplot_ax import PyplotAx
import matplotlib.patches as patches


class Plotter():
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.pyplot_ax = PyplotAx(xmin, xmax, ymin, ymax)

    def set_step(self, step, step_minor):
        self.pyplot_ax.set_step(step, step_minor)

    def prepare_plotting(self):  # ???
        self.ax = self.pyplot_ax.ax()

    def draw_box(self, box, color='k'):
        llc, w, h = box.border_definition()
        rect = patches.Rectangle(llc, w, h, linewidth=.3, edgecolor=color, facecolor='none')
        self.ax.add_patch(rect)

    def draw_points(self, xs, ys, color='k'):
        self.ax.scatter(xs, ys, c=color)

    def draw_line(self, x1, y1, x2, y2,  color='black'):
        xs = [x1, x2]
        ys = [y1, y2]
        plt.plot(xs, ys, color=color, linewidth=1, alpha=0.5)

    def scatter(self, xs, ys):
        plt.scatter(xs, ys, s=1)


    def show(self):
        plt.subplots_adjust(wspace=0, hspace=0)
        plt.tight_layout()
        plt.show()
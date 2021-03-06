import numpy as np
from matplotlib import pyplot as plt


class PyplotAx:
    def __init__(self, xmin=-100, xmax=100, ymin=-100, ymax=100):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.ticks_step_major = (xmax - xmin) // 4
        self.ticks_step_minor = self.ticks_step_major // 2
        self.grid_alpha = None
        self.spine_alpha = None

    def set_spine_and_grid(self, ticks_step_major, ticks_step_minor, grid_alpha, spine_alpha):
        self.ticks_step_major = ticks_step_major
        self.ticks_step_minor = ticks_step_minor
        self.grid_alpha = grid_alpha
        self.spine_alpha = spine_alpha

    def create_ticks_major(self):
        x_start = int(self.xmin / self.ticks_step_major) * self.ticks_step_major
        x_stop = int(self.xmax / self.ticks_step_major) * self.ticks_step_major
        x_ticks = [x for x in range(x_start, x_stop + 1, self.ticks_step_major) if x != 0]

        y_start = int(self.ymin / self.ticks_step_major) * self.ticks_step_major
        y_stop = int(self.ymax / self.ticks_step_major) * self.ticks_step_major
        y_ticks = [y for y in range(y_start, y_stop + 1, self.ticks_step_major) if y != 0]

        return x_ticks, y_ticks

    def create_ticks_minor(self):
        x_start = int(self.xmin / self.ticks_step_minor) * self.ticks_step_minor
        x_stop = int(self.xmax / self.ticks_step_minor) * self.ticks_step_minor
        x_ticks = [x for x in range(x_start, x_stop + 1, self.ticks_step_minor) if x != 0]

        y_start = int(self.ymin / self.ticks_step_minor) * self.ticks_step_minor
        y_stop = int(self.ymax / self.ticks_step_minor) * self.ticks_step_minor
        y_ticks = [y for y in range(y_start, y_stop + 1, self.ticks_step_minor) if y != 0]

        return x_ticks, y_ticks

    def ax(self):
        _, ax = plt.subplots(figsize=(6, 6))

        # ax.grid(alpha=0.0)

        # Set identical scales for both axes.
        ax.set(xlim=(self.xmin-1, self.xmax+1), ylim=(self.ymin-1, self.ymax+1), aspect='equal')

        # Set bottom and left spines as x and y axes of coordinate system.
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')

        # Remove top and right spines.
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.tick_params(axis='both', which=u'both', length=3, color='#00000080', labelsize=7)
        # ax.axhline(alpha=0)

        # Major ticks
        x_ticks_major, y_ticks_major = self.create_ticks_major()
        ax.set_xticks(x_ticks_major)
        ax.set_yticks(y_ticks_major)

        # Minor ticks
        x_ticks_minor, y_ticks_minor = self.create_ticks_minor()
        ax.set_xticks(x_ticks_minor, minor=True)
        ax.set_yticks(y_ticks_minor, minor=True)

        # spine_alpha = 0.5
        for axis in ['bottom', 'left']:
            ax.spines[axis].set_alpha(self.spine_alpha)

        plt.setp(ax.get_xticklabels(), alpha=self.spine_alpha)
        plt.setp(ax.get_yticklabels(), alpha=self.spine_alpha)

        show_xy_labels = False
        if show_xy_labels:
            ax.set_ylabel('y values', fontname="Arial", fontsize=12)
            ax.set_xlabel('x values', fontname="Arial", fontsize=12)

        draw_grid_lines = True
        if draw_grid_lines:
            # Draw major and minor grid lines.
            ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=self.grid_alpha)

        draw_arrows = False
        if draw_arrows:
            # Draw arrows at the end of the x- and y-axes.
            arrow_fmt = dict(markersize=4, color='black', clip_on=False)
            ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
            ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

        return ax

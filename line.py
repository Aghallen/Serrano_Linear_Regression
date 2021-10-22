from enum import Enum
import math


class Location(Enum):
    ABOVE = 0
    BELOW = 1


class Line():
    def __init__(self):
        # y = slope * x + intercept
        self.slope = None
        self.intercept = None
        # Ax + By + C = 0
        self.a = None
        self.b = None
        self.c = None

    def create_by_slope_intercept(self, slope, intercept):
        # y = slope * x + intercept
        self.slope = slope; self.intercept = intercept
        # Ax + By + C = 0
        self.a = -slope; self.b = 1; self.c = -intercept
        return self

    def create_by_ax_bx_c(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.slope = -a / b
        self.intercept = -c / b
        return self

    def clone(self):
        my_self = self.__class__()
        my_self.create_by_slope_intercept(self.slope, self.intercept)
        return my_self

    def f(self, x):
        return self.slope * x + self.intercept

    def f_inverse(self, y):
        return (y - self.intercept) / self.slope

    def clip_point(self, x_clip_limit, y_clip_min, y_clip_max):
        y_clip_limit = self.f(x_clip_limit)
        if y_clip_limit > y_clip_max:
            y = y_clip_max
            x = self.f_inverse(y_clip_max)
        elif y_clip_limit < y_clip_min:
            y = y_clip_min
            x = self.f_inverse(y_clip_min)
        else:
            y = y_clip_limit
            x = x_clip_limit

        return x, y

    def clip_line(self, frame):
        x1, y1 = self.clip_point(frame.xmin, frame.ymin, frame.ymax)
        x2, y2 = self.clip_point(frame.xmax, frame.ymin, frame.ymax)
        return x1, y1, x2, y2

    def coords_clipped_by_window(self, plot_frame):
        xmin = plot_frame.xmin
        xmax = plot_frame.xmax
        ymin = plot_frame.ymin
        ymax = plot_frame.ymax
        x1, y1 = self.clip_point(xmin, ymin, ymax)
        x2, y2 = self.clip_point(xmax, ymin, ymax)
        return x1, y1, x2, y2

    def coords_clipped_by_y(self, y_min, y_max):
        if self.slope > 0:
            x1 = self.f_inverse(y_min)
            y1 = y_min
            x2 = self.f_inverse(y_max)
            y2 = y_max
        else:
            x1 = self.f_inverse(y_max)
            y1 = y_max
            x2 = self.f_inverse(y_min)
            y2 = y_min

        return x1, y1, x2, y2

    def move_parallelly(self, distance, location=None):
        delta_intercept = math.sqrt(1 + self.slope * self.slope) * distance
        print(f'distance: {distance}')
        print(f'delta_intercept: {delta_intercept}')
        print(f'self.intercept + delta_intercept: {self.intercept + delta_intercept}')
        self.create_by_slope_intercept(self.slope, self.intercept + delta_intercept)


if __name__ == '__main__':
    line1 = Line()
    slope1 = 3
    intercept1 = 5
    print(f'slope: {slope1} intercept: {intercept1}')
    line1.create_by_slope_intercept(slope1, intercept1)

    a = line1.a; b = line1.b; c = line1.c
    print(f'a: {a} b: {b} c: {c}')

    line2 = Line()
    line2.create_by_ax_bx_c(a, b, c)
    slope2 = line2.slope
    intercept2 = line2.intercept
    print(f'slope: {slope2} intercept: {intercept2}')


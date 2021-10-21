

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
        self.slope = slope
        self.intercept = intercept
        self.a = -slope
        self.b = 1
        self.c = -intercept
        return self

    def create_by_ax_bx_c(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.slope = -a / b
        self.intercept = -c / b
        return self

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

    def clip_line(self, xmin, xmax, ymin, ymax):
        x1, y1 = self.clip_point(xmin, ymin, ymax)
        x2, y2 = self.clip_point(xmax, ymin, ymax)
        return x1, y1, x2, y2

    # def coordinates_clip_at_spines_OLD(self, xmin, xmax, ymin, ymax):
    #     y = self.f(xmin)
    #     if y > ymax:
    #         y1 = ymax
    #         x1 = self.f_inverse(ymax)
    #     elif y < ymin:
    #         y1 = ymin
    #         x1 = self.f_inverse(ymin)
    #     else:
    #         y1 = y
    #         x1 = xmin
    #
    #     y = self.f(xmax)
    #     if y > ymax:
    #         y2 = ymax
    #         x2 = self.f_inverse(ymax)
    #     elif y < ymin:
    #         y2 = ymin
    #         x2 = self.f_inverse(ymin)
    #     else:
    #         y2 = y
    #         x2 = xmax
    #
    #     return x1, y1, x2, y2


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


import numpy as np


class Linear:
    @classmethod
    def parameters(cls, x_values, y_values):
        delta_y = np.max(y_values) - np.min(y_values)
        delta_x = np.max(x_values) - np.min(x_values)
        slope = delta_y / delta_x


        y_mean = np.mean(y_values)
        x_mean = np.mean(x_values)

        # Solve for b: y = m*x + b => b = y - m*x
        intercept = y_mean - slope * x_mean

        return slope, intercept

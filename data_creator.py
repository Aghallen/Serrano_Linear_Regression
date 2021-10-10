import numpy as np


class DataCreator():
    def __init__(self, x_values, slope=2, intercept=5):
        x_list = []
        y_list = []

        for x in x_values:
            y = intercept + slope * x
            x_list.append(x)
            y_list.append(y)
            x += 1

        self.x_values = np.array(x_list)
        self.y_values = np.array(y_list)

    def add_noise(self, dependent=30, independent=50, seed=None):
        if not seed is None:
            np.random.seed(seed)

        temp = []
        for y_value in self.y_values:
            dependent_noise = y_value * np.random.randint(dependent) / 100.0
            independent_noise = np.random.randint(independent)
            y_with_noise = y_value + dependent_noise + independent_noise
            temp.append(y_with_noise)

        self.y_values = np.array(temp)

    def batch(self, batch_size=-1):
        if batch_size < 0:
            # Returns all values.
            return self.x_values, self.y_values
        else:
            # Returns a slice of x_values and a slice of the corresponding y_values.
            indexes = np.array(list(range(len(self.x_values))))
            np.random.shuffle(indexes)
            random_indexes = indexes[:batch_size]
            random_indexes.sort()

            x_values_slice = self.x_values[random_indexes]
            y_values_slice = self.y_values[random_indexes]

            return x_values_slice, y_values_slice

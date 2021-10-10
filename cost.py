import numpy as np

class Cost:
    @classmethod
    def rmse(cls, observed, predicted):
        diff = np.subtract(observed, predicted)
        squared = np.square(diff)
        sum_of_squared = sum(squared)
        mean_squared_error = sum_of_squared / len(observed)
        ret_value = np.sqrt(mean_squared_error)
        return ret_value

from scipy import stats
from data_creator import DataCreator
from cost import Cost

class LeastSquareMethod:
    @classmethod
    def show(cls, x_values, y_values):
        # Use lsm (least square method) to calculate slope and intercept for the observed values.
        slope_lsm, intercept_lsm, r, p, std_err = stats.linregress(x_values, y_values)

        # Create list of y-values based on lsm.
        data_creator = DataCreator(x_values, intercept_lsm, slope_lsm)
        dummy, y_lsm = data_creator.batch()

        # Calculate cost as RMSE (Root-Mean-Square Error).
        cost = Cost.rmse(y_values, y_lsm)
        print(f'\nLinear least-squares for comparison.')
        print(f'slope: {slope_lsm:.2f} intercept: {intercept_lsm:.2f} cost: {cost:.2f}')


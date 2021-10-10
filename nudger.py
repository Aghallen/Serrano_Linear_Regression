class Nudger:
    @classmethod
    def nudge(cls, x, y_obs, y_pred):
        if x > 0:
            if y_obs > y_pred:
                intercept_factor =  slope_factor= 1
            else:
                intercept_factor = slope_factor = -1
        else:
            if y_obs > y_pred:
                intercept_factor = 1
                slope_factor = -1
            else:
                intercept_factor = -1
                slope_factor = 1

        return slope_factor, intercept_factor

    # The below nudge2 doesn't work as expected.
    @classmethod
    def nudge2(cls, x, y_obs, y_pred):
        vertical_distance = y_obs - y_pred
        slope_factor = x * vertical_distance
        intercept_factor = vertical_distance
        return slope_factor, intercept_factor

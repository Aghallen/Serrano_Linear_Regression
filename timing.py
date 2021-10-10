class Timing:
    @classmethod
    def time_to_print(cls, epoch):
        if epoch > 1e4:
            result = not epoch % 2e4  # Every 20 000:th
        elif epoch > 1e3:
            result = not epoch % 2e3  # Every 2000:th
        elif epoch > 1e2:
            result = not epoch % 2e2  # Every 200:th
        elif epoch > 1e1:
            result = not epoch % 2e1  # Every 20:th
        else:
            result = True

        return result
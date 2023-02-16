def r_squared(measured, predicted):
    '''Assumes measured a one-dimensional array of measured values
               predicted a one-dimensional array of predicted values
       Returns coefficient of determination'''
    # r_squared mean how much data can be explained by the model
    estimated_error = ((predicted - measured) ** 2).sum()
    mean_of_measured = measured.sum() / len(measured)
    variability = ((measured - mean_of_measured) ** 2).sum()
    return 1 - estimated_error / variability

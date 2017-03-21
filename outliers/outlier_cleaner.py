#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    res = []

    for index in range(0, len(predictions)):
        res.append((ages[index][0], net_worths[index][0], abs(predictions[index][0] - net_worths[index][0])))

    sorted_res = sorted(res, key = lambda t: t[2] , reverse = True)

    return sorted_res[int(len(ages)*0.1):]


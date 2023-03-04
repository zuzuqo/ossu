def accuracy(true_pos, false_pos, true_neg, false_neg):
    numerator = true_pos + true_neg
    denominator = true_pos + true_neg + false_pos + false_neg
    return numerator / denominator


def sensitivity(true_pos, false_neg):
    '''Returns the proportion of positives that are correctly identified as such'''
    try:
        return true_pos / (true_pos + false_neg)
    except ZeroDivisionError:
        return float('nan')


def specificity(true_neg, false_pos):
    '''Returns the proportion of negatives that are correctly identified as such'''
    try:
        return true_neg / (true_neg + false_pos)
    except ZeroDivisionError:
        return float('nan')


def pos_pred_val(true_pos, false_pos):
    '''Returns the probability that an example classified as positive is truly positive'''
    try:
        return true_pos / (true_pos + false_pos)
    except ZeroDivisionError:
        return float('nan')


def neg_pred_val(true_neg, false_neg):
    '''Returns the probability that an example classified as negative is truly negative'''
    try:
        return true_neg / (true_neg + false_neg)
    except ZeroDivisionError:
        return float('nan')


def get_stats(true_pos, false_pos, true_neg, false_neg, to_print=True):
    accur = accuracy(true_pos, false_pos, true_neg, false_neg)
    sens = sensitivity(true_pos, false_neg)
    spec = specificity(true_neg, false_pos)
    ppv = pos_pred_val(true_pos, false_pos)
    if to_print:
        print(f'\tAccuracy = {round(accur, 3)}')
        print(f'\tSensitivity = {round(sens, 3)}')
        print(f'\tSpecificity = {round(spec, 3)}')
        print(f'\tPos.Pred.Val. = {round(ppv, 3)}')
    return accur, sens, spec, ppv

def variance(x: list):
    '''Дисперсия из теории вероятности'''
    mean = sum(x) / len(x)
    tot = 0
    for i in x:
        tot += (i - mean) ** 2
    return tot / len(x)


def standard_deviation(x: list):
    '''Стандартное (среднеквадратичное) отклонение'''
    return variance(x) ** .5


def coefficient_variation(x: list):
    mean = sum(x) / len(x)
    try:
        return standard_deviation(x) / mean
    except ZeroDivisionError:
        return float('nan')

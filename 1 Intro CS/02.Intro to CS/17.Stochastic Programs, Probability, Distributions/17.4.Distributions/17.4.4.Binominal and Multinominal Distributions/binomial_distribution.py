from math import factorial


def binomial_coeff(num_trials, num_repeats):
    return factorial(num_trials) / (factorial(num_repeats) * factorial(num_trials - num_repeats))


def binomial_distribution(num_trials, num_repeats, probably, r=3):
    bc = binomial_coeff(num_trials, num_repeats)
    return round(bc * (probably ** num_repeats) * ((1 - probably) ** (num_trials - num_repeats)), r)
def square_root_exhaustive(x: float, epsilon: float):
    # using exhaustive enumeration
    '''Assumes x and epsilon are positive floats & epsilon < 1
       Retruns a y such that y*y is within epsilon of x'''
    step = epsilon ** 2
    ans = .0
    while abs(ans ** 2 - x) >= epsilon and ans * ans <= x:
        ans += step
    if ans * ans > x:
        raise ValueError
    return ans


def square_root_bi(x: float, epsilon: float):
    # using bisection search
    '''Assumes x and epsilon are positive floats & epsilon < 1
       Retruns a y such that y*y is within epsilon of x'''
    low = .0
    high = max(1.0, x)
    ans = (high + low) / 2
    while abs(ans ** 2 - x) >= epsilon:
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

# requires roughly one billion iterations of while loop
# square_root_exhaustive(100, 0.0001)
# requires roughly 20 iterations of slightly more complex while loop
square_root_bi(100, 0.0001)

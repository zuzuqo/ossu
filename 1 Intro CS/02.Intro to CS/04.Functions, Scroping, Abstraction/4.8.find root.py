def find_root_bounds(x, power):
    '''
    :param x: float
    :param power: positive int
    :return: low and high such that low**power <= x and high**power >= x
    '''
    low = min(-1, x)
    high = max(1, x)
    return low, high


def bisection_solve(x, power, epsilon, low, high):
    '''
    :param x: float
    :param power: positive int
    :param epsilon: positive float and != 0
    :param low: float
    :param high: float
    :return: ans such that ans**power within epsilon of x
    '''
    ans = (high + low) / 2
    while abs(ans ** power - x) >= epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans


def find_root(x, power, epsilon):
    '''
    :param x: float
    :param power: int
    :param epsilon: float
    :return:
    '''
    if x < 0 and power % 2 == 0:
        return None
    low, high = find_root_bounds(x, power)
    return bisection_solve(x, power, epsilon, low, high)


def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = 'No root exists'
                else:
                    val = 'Okay'
                    if abs(result ** p - x) > e:
                        val = 'Bad'
                print(f'x = {x}, power = {p}, epsilon = {e}: {val}')


x_vals = (0, 25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)
test_find_root(x_vals, powers, epsilons)

def f(x: int):
    '''Assume x is an int > 0'''
    ans = 0

    # Loop that takes constant time
    # 1000
    for i in range(1000):
        ans += 1
    print(f'Number of additions so far {ans}')

    # Loop that takes time x
    # x
    for i in range(x):
        ans += 1
    print(f'Number of additions so far {ans}')

    # Nested loops take time x**2
    # 2 * x**2
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1
    print(f'Number of additions so far {ans}')
    return ans


# f(10)
# f(1000)


def g(L, e):
    '''L a list of ints, e is an int'''
    # 100 * len(L) in worst case
    for i in range(100):
        for e1 in L:
            if e1 == e:
                return True
    return False


def h(L, e):
    '''L a list of ints, e is an int'''
    # e * len(L) in worst case
    for i in range(e):
        for e1 in L:
            if e1 == e:
                return True
    return False

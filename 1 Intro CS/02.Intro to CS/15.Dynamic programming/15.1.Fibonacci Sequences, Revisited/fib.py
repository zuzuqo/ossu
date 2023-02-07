# bad example
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


def fib_memoization(n: int, memo: dict = None):
    if n < 0:
        return None
    if memo is None:
        memo = {}
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
        memo[n] = result
        return result


def fib_tabular(n: int):
    if n < 0:
        return None
    tab = [1] * (n + 1)
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]
    return tab[n]


if __name__ == '__main__':
    print(fib_memoization(120))
    print(fib_tabular(120))

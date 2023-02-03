
def fib(n):
    global num_fib_calls
    num_fib_calls += 1

    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def test_fib(n):
    global num_fib_calls
    num_fib_calls = 0

    for i in range(n + 1):
        print(f'fib of {i} = {fib(i)}')

    print(f'Count calls: {num_fib_calls} times')


if __name__ == '__main__':
    test_fib(10)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def test_fib(n):
    for i in range(n+1):
        print(f'fib of {i} = {fib(i)}')


if __name__ == '__main__':
    test_fib(10)
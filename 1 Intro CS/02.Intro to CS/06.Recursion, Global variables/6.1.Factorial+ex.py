def fact_rec(n):
    if n == 1:
        return n
    else:
        return n * fact_rec(n - 1)


def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)

print(harmonic_sum(3))

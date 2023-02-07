import sys


def make_change(coin_vals: [int], var: int) -> int or None:
    '''Return the minimum number of coins needed to have a set of coins
       the values of which sum to var.
       Coins may be used more than once'''
    # validation
    coin_vals.sort()
    if coin_vals[0] != 1:
        return None
    for i in coin_vals:
        if i < 0:
            return None
    # solution
    table = [0 for i in range(var + 1)]
    for i in range(1, var + 1):
        table[i] = sys.maxsize

    for i in range(1, var + 1):
        for j in range(len(coin_vals)):
            if coin_vals[j] <= i:
                sub_res = table[i - coin_vals[j]]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1
    if table[var] == sys.maxsize:
        return var
    return table[var]


if __name__ == '__main__':
    coins = [9, 6, 5, 1]
    v = 12
    print(make_change(coins, v))

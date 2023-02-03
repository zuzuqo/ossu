def get_binary_rep(n, num_digits):
    '''Assumes n and num_digits are non-negative ints
       Returns a str of length num_digits that is a binary representation of n'''
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    if len(result) > num_digits:
        raise ValueError('not enough digits')
    for i in range(num_digits - len(result)):
        result = '0' + result
    return result

# O (2 ** len(L))
def get_powerset(L):
    '''Assumes L is a list
       Returns a list of lists that contains all possible combinations of the elements of L.
       E.g., if L is [1,2] it will return [[], [1], [2], [1, 2]]'''
    powerset = []
    for i in range(0, 2 ** len(L)):
        bin_str = get_binary_rep(i, len(L))
        subset = []
        for j in range(len(L)):
            if bin_str[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset


# print(get_powerset(['x', 'y', 'z', 'a']))

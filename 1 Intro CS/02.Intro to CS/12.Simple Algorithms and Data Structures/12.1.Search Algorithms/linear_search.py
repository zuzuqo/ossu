def search(L, e):
    '''L is a sorted list
       Retrun True if e is in L and False otherwise'''
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


if __name__ == '__main__':
    my_list = [1, 6, 3, 6, 4]

    print(search(my_list, 5))
    print(search(my_list, 2))
    print(search(my_list, 1))

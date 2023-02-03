def search(L, e):
    '''L is a sorted list
       Returns True if e is in L and False otherwise'''

    # O (log(len(L)))
    def bin_search(L, e, low, high):
        # Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bin_search(L, e, low, mid - 1)
        else:
            return bin_search(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)


if __name__ == '__main__':
    my_list = [1, 6, 3, 6, 4]

    print(search(my_list, 5))
    print(search(my_list, 2))
    print(search(my_list, 1))

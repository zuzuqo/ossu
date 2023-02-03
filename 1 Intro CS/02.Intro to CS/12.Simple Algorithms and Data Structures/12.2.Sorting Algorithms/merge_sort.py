def merge(left: list, right: list, compare: callable) -> list:
    '''Assumes left and right are sorted lists and compare defines an ordering on the elements
       Returns a new sorted (by compare) list containing the same elements as (left + right) would contain.'''
    result = []
    i, j, = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(l: list, compare: callable = lambda x, y: x < y):
    '''compare defines an ordering on elements of l
       Returns a new sorted list with the same elements as l'''
    # O (len(l) * log(len(l))), but can be an issue for large lists
    if len(l) < 2:
        return l[:]
    else:
        middle = len(l) // 2
        left = merge_sort(l[:middle], compare)
        right = merge_sort(l[middle:], compare)
        return merge(left, right, compare)


if __name__ == '__main__':
    my_list = [2, 1, 4, 6, 5, 3, 6]
    print(merge_sort(my_list))
    print(merge_sort(my_list, lambda x, y: x > y))

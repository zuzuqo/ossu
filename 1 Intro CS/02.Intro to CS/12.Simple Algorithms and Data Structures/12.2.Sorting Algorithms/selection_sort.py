def sel_sort(l: list):
    '''Sorts l in ascending order'''
    # O (len(l)^2)
    suffix_start = 0
    while suffix_start != len(l):
        # look at each element in suffix
        for i in range(suffix_start, len(l)):
            if l[i] < l[suffix_start]:
                # swap position of elements
                l[suffix_start], l[i] = l[i], l[suffix_start]
        suffix_start += 1


if __name__ == '__main__':
    my_list = [1, 6, 3, 6, 4]
    sel_sort(my_list)

    print(my_list)

def shell_sort(alist):
    sublist_count = 0
    i = 1
    while sublist_count < len(alist):
        sublist_count = pow(2, i) - 1
        i += 1



    # sublist_count = len(alist)//2

    while sublist_count > 0:
        for start_pos in range(sublist_count):
            gap_insertion_sort(alist, start_pos, sublist_count)

        print('after increments of size', sublist_count, 'The list is:', alist)

        sublist_count //= 2


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        current_val = alist[i]
        position = i

        while position >= gap and current_val < alist[position - gap]:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = current_val

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]

shell_sort(data)

print('final', data)
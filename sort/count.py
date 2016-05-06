def find_max(alist):
    max_index = 0
    for index in range(1, len(alist)):
        if alist[max_index] < alist[index]:
            max_index = index

    return alist[max_index]


def count_sort(alist):
    max_value = find_max(alist)
    count = [0] * (max_value + 1)

    for index in range(len(alist)):
        item = alist[index]
        count[item] += 1

    total = 0
    for index in range(len(count)):
        old_count = count[index]
        count[index] = total
        total += old_count

    output = [0] * len(alist)

    for item in alist:
        output[count[item]] = item
        count[item] += 1

    return output


data = [0, 54, 26, 0, 93, 17, 77, 31, 44, 55, 20]

print('final', count_sort(data))

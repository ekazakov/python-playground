def insertion_sort(alist):
    for i in range(1, len(alist)):
        pos = i
        current_value = alist[pos]

        while pos > 0 and current_value < alist[pos - 1]:
            alist[pos] = alist[pos - 1]
            pos -= 1

        alist[pos] = current_value
        print('>', alist)
    return alist


data = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(insertion_sort(data))

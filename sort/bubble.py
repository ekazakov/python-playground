def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(len(alist) - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

    return alist


data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# data.sort()
# data.reverse()

print(bubble_sort(data))

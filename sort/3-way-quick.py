# 3-way partitioning quick sort
def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, lo, hi):
    if hi <= lo:
        return

    lt = lo
    index = lo + 1
    gt = hi

    pivot_value = alist[lo]

    while index <= gt:
        if alist[index] < pivot_value:
            alist[lt], alist[index] = alist[index], alist[lt]
            index += 1
            lt += 1
        elif alist[index] > pivot_value:
            alist[index], alist[gt] = alist[gt], alist[index]
            gt -= 1
        else:
            index += 1

    # print('>', alist)

    quick_sort_helper(alist, lo, lt - 1)
    quick_sort_helper(alist, gt + 1, hi)

data = [54, 802, 26, 11, 93, 17, 54, 54, 77, 11, 31, 2, 44, 55, 20]
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]

quick_sort(data)
quick_sort(data1)

print('final:', data)
print('final:', data1)

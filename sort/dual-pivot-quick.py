"""
1. For small arrays (length < 17), use the Insertion sort algorithm.
2. Choose two pivot elements P1 and P2.
   We can get, for example, the first element a[left] as P1 and the last element a[right] as P2.
3. P1 must be less than P2, otherwise they are swapped. So, there are the following parts:
  * part I with indices from left+1 to L–1 with elements, which are less than P1,
  * part II with indices from L to K–1 with elements, which are greater or equal to P1
    and less or equal to P2,
  * part III with indices from G+1 to right–1 with elements greater than P2,
  * part IV contains the rest of the elements to be examined with indices from K to G.
4. The next element a[K] from the part IV is compared with two pivots P1 and P2,
   and placed to the corresponding part I, II, or III.
5. The pointers L, K, and G are changed in the corresponding directions.
6. The steps 4 - 5 are repeated while K ≤ G.
7. The pivot element P1 is swapped with the last element from part I, t
   he pivot element P2 is swapped with the first element from part III.
8. The steps 1 - 7 are repeated recursively for every part I, part II, and part III.
"""


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, low, high):
    if high <= low:
        return

    lt = low + 1
    gt = high - 1

    index = lt

    if alist[low] > alist[high]:
        alist[low], alist[high] = alist[high], alist[low]

    pivot_value_1 = alist[low]
    pivot_value_2 = alist[high]

    while index <= gt:
        if alist[index] < pivot_value_1:
            alist[index], alist[lt] = alist[lt], alist[index]
            lt += 1
            index += 1
        elif alist[index] > pivot_value_2:
            alist[index], alist[gt] = alist[gt], alist[index]
            gt -= 1
        else:
            index += 1

    lt -= 1
    gt += 1

    alist[low], alist[lt] = alist[lt], alist[low]
    alist[high], alist[gt] = alist[gt], alist[high]

    quick_sort_helper(alist, low, index - 1)
    quick_sort_helper(alist, index + 1, gt - 1)
    quick_sort_helper(alist, gt + 1, high)


data = [54, 802, 26, 11, 93, 17, 54, 54, 77, 11, 31, 2, 44, 55, 20]
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]

quick_sort(data)
quick_sort(data1)

print('final:', data)
print('final:', data1)
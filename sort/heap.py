# def heap_sort(alist):
#     def shift_down(alist, i, j):
#         while i * 2 + 1 < j:
#             if i * 2 + 1 == j - 1 or alist[i*2 + 1] > alist[i*2 + 2]:
#                 max_child = i * 2 + 1
#             else:
#                 max_child = i * 2 + 2
#             if alist[i] < alist[max_child]:
#                 alist[i], alist[max_child] = alist[max_child], alist[i]
#                 i = max_child
#             else: break
#
#     for i in range(int(len(alist)/ 2 - 1), -1, -1):
#         shift_down(alist, i, len(alist))
#
#     for i in range(len(alist) - 1, 0, -1):
#         alist[0], alist[i] = alist[i], alist[0]
#         shift_down(alist, 0, i)
#
#
# data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#
# heap_sort(data)
#
# print('final', data)

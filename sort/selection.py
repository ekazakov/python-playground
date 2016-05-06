def selection_sort(alist):
    for fill_slot in range(len(alist) - 1, 0, -1):
        position_of_max = 0

        for location in range(1, fill_slot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        alist[fill_slot], alist[position_of_max] = alist[position_of_max], alist[fill_slot]

    return alist


data = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(selection_sort(data))

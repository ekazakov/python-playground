class MyBinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i //= 2

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            min_child_index = self.min_child(i)

            if self.heap_list[i] > self.heap_list[min_child_index]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child_index]
                self.heap_list[min_child_index] = tmp
            i = min_child_index

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def del_min(self):
        value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)

        return value

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]

        while i > 0:
            self.percolate_down(i)
            i -= 1



class BinaryHeap(object):
    """
    BinaryHeap() creates a new, empty, binary heap.
    insert(k) adds a new item to the heap.
    findMin() returns the item with the minimum key value, leaving item in the heap.
    delMin() returns the item with the minimum key value, removing the item from the heap.
    isEmpty() returns true if the heap is empty, false otherwise.
    size() returns the number of items in the heap.
    buildHeap(list) builds a new heap from a list of keys.
    """
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def __perc_up(self, i):
        while i // 2 > 0:
            # If the current value is less than its parent, perc up
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp

            i = i // 2

    def __perc_down(self, i):
        while (i * 2) <= self.current_size:
            min_child = self.__min_child(i)
            if self.heap_list[i] > self.heap_list:
                temp = self.heap_list[min_child]
                self.heap_list[i] = self.heap_list[min_child]
                self.heap_list[min_child] = temp
            i = min_child

    def __min_child(self, i):
        if i * 2 + i > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1]:
                return i * 2
            else:
                return (i * 2) + 1

    def insert(self, k):
        self.heapList.append(k)
        self.current_size += 1
        self.__perc_up(self.current_size)

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.heap_list.__perc_down(1)

        return ret_val

    def build_heap(self, elements):
        i = len(elements) // 2
        self.current_size = len(elements)
        self.heap_list = [0] + elements[:]
        while i > 0:
            self.__perc_down(i)
            i = i - 1

    def size(self):
        return self.current_size

    def is_empty(self):
        return len(self.heap_list) == 0

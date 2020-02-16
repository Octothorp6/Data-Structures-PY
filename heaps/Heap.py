class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, data):
        self.heap.append(data)
        self.__fix_heap_above(self.size)
        self.size += 1

    def delete(self, index):
        if self.is_empty():
            raise Exception("The heap is empty.")

        parent = self.__get_parent(index)
        deleted = self.heap[index]

        self.heap[index] = self.heap[len(self.heap) - 1]
        if (index == 0) or (self.heap[index] < self.heap[parent]):
            self.__fix_heap_below(index, len(self.heap) - 1)
        else:
            self.__fix_heap_above(index)

        self.size -= 1

        return deleted

    def is_empty(self):
        return len(self.heap) == 0

    def __fix_heap_above(self, index):
        new_value = self.heap[index]

        while (index > 0) and (new_value > self.heap[self.__get_parent(index)]):
            self.heap[index] = self.heap[self.__get_parent(index)]
            index = self.__get_parent(index)

        self.heap[index] = new_value

    def __fix_heap_below(self, index, last_heap_index):
        while index <= last_heap_index:
            left_child = self.__get_child(index, True)
            right_child = self.__get_child(index, False)
            if left_child <= right_child:
                if right_child > last_heap_index:
                    child_to_swap = left_child
                else:
                    child_to_swap = left_child if self.heap[left_child] > self.heap[right_child] else right_child

                if self.heap[index] < self.heap[child_to_swap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[child_to_swap]
                    self.heap[child_to_swap] = temp
                else:
                    break

                index = child_to_swap
            else:
                break

    @staticmethod
    def __get_parent(index):
        return (index - 1) // 2

    @staticmethod
    def __get_child(index, left):
        if left:
            return (2 * index) + 1
        else:
            return (2 * index) + 2

    def print_heap(self):
        for i in range(len(self.heap)):
            print(self.heap[i], end=", ")
        print("")

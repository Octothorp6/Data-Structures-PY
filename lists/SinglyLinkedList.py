class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        temp = Node(data)
        if self.is_empty():
            self.head = temp
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = temp

        self.size += 1

    def is_empty(self):
        return self.size == 0

    def print_list(self):
        node = self.head

        while node.next is not None:
            print(node.data, end=", ")
            node = node.next
        print(node.data)

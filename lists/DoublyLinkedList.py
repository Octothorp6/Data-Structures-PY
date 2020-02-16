class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_front(self, data):
        node = Node(data)
        if self.is_empty():
            tail = node
        else:
            self.head.previous = node
            node.next = self.head

        self.head = node
        self.size += 1

    def is_empty(self):
        return self.size == 0

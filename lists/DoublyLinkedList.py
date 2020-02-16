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
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head

        self.head = node
        self.size += 1

    def insert(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
            node.previous = self.tail

        self.tail = node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return

        removed = self.head

        if self.head.next is None:
            self.tail = None
        else:
            self.head.next.previous = None

        self.head = self.head.next
        self.size -= 1
        removed.next = None

        return removed

    def remove_last(self):
        if self.is_empty():
            return

        removed = self.tail

        if self.tail.previous is None:
            self.head = None
        else:
            self.tail.previous.next = None

        self.tail = self.tail.previous
        self.size -= 1
        removed.previous = None

        return removed

    def is_empty(self):
        return self.size == 0

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data, end=", ")
            current = current.next

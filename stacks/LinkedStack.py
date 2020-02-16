from _collections import deque


class LinkedStack:
    def __init__(self):
        self.stack = deque([])

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
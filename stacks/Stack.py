class Stack:
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, data):
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")

        element = self.stack[self.top - 1]
        self.top -= 1
        self.stack[self.top] = None

        return element

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")

        return self.stack[self.top - 1]

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        for i in range(len(self.stack))[::-1]:
            print(self.stack[i])

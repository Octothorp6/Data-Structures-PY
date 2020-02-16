class Queue:
    def __init__(self):
        self.queue = []
        self.back = 0

    def add(self, data):
        self.queue.append(data)
        self.back += 1

    def remove(self):
        if self.is_empty():
            raise Exception("The queue is empty.")

        removed = self.queue.pop(0)
        self.back -= 1

        if self.is_empty():
            self.back = 0

        return removed

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty.")

        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def print_queue(self):
        for i in self.queue:
            print(i, end=", ")
        print("")

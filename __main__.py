from trees import BinarySearchTree
from lists import SinglyLinkedList, DoublyLinkedList
from stacks import Stack, LinkedStack
from queues import Queue
from heaps import BinaryHeap


def make_tree():
    tree = BinarySearchTree()
    tree.put("mak", 50)
    tree.put("bop", 60)
    tree.put("sdd", 34)
    tree.put("elo", 36)

    print(tree.length())


def linked_list():
    singly_linked = SinglyLinkedList()
    singly_linked.add(2)
    singly_linked.add(44)
    singly_linked.add(24)

    singly_linked.print_list()


def doubly_linked_list():
    doubly_linked = DoublyLinkedList()
    doubly_linked.insert(32)
    doubly_linked.insert(34)
    doubly_linked.insert(45)
    doubly_linked.insert(47)
    doubly_linked.insert(87)

    doubly_linked.print_list()


def make_stack():
    stack = Stack()
    stack.push(23)
    stack.push(35)
    stack.push(56)
    stack.push(32)

    print(f"Stack: {stack.items}")


def make_queue():
    queue = Queue()
    queue.enqueue(23)
    queue.enqueue(45)
    queue.enqueue(58)
    queue.enqueue(34)
    queue.enqueue(45)

    print(f"Queue: {queue.items}")


def make_heap():
    heap = BinaryHeap()
    heap.insert(23)
    heap.insert(45)
    heap.insert(32)
    heap.insert(27)
    heap.insert(36)
    heap.insert(74)

    print(f"Heap: {heap.heap_list}")


if __name__ == '__main__':
    linked_list()
    doubly_linked_list()
    make_queue()
    make_heap()
    make_tree()

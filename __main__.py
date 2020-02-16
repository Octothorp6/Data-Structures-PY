from trees import Tree
from lists import SinglyLinkedList, DoublyLinkedList
from stacks import Stack, LinkedStack


def make_tree():
    tree = Tree()
    tree.insert(50)
    tree.insert(60)
    tree.insert(30)
    tree.insert(25)
    tree.insert(27)
    tree.insert(71)
    tree.insert(66)

    tree.traverse_in_order()


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

    stack.print_stack()


if __name__ == '__main__':
    make_stack()

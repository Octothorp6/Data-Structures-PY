from trees.Tree import Tree
from lists.SinglyLinkedList import SinglyLinkedList


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


if __name__ == '__main__':
    linked_list()

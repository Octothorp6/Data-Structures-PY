from trees.Tree import Tree


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


if __name__ == '__main__':
    make_tree()

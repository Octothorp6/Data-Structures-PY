from . import TreeNode


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert(value)

    def get(self, value):
        if self.root is not None:
            return self.root.get(value)

        return

    def delete(self, subtree_root: TreeNode, value):
        if subtree_root is None:
            return

        if value < subtree_root.data:
            subtree_root.left_child = self.delete(subtree_root.left_child, value)
        elif value > subtree_root.data:
            subtree_root.right_child = self.delete(subtree_root.right_child, value)
        else:
            if subtree_root.left_child is None:
                return subtree_root.right_child
            elif subtree_root.right_child is None:
                return subtree_root.left_child

            subtree_root.data = subtree_root.right_child.min()
            subtree_root.right_child = self.delete(subtree_root.right_child, subtree_root.data)

        return subtree_root

    def min(self):
        if self.root is None:
            return -1
        else:
            return self.root.min()

    def max(self):
        if self.root is None:
            return -1
        else:
            return self.root.max()

    def traverse_in_order(self):
        if self.root is not None:
            return self.root.traverse_in_order()

    def traverse_pre_order(self):
        if self.root is not None:
            return self.root.traverse_pre_order()

    def traverse_post_order(self):
        if self.root is not None:
            return self.root.traverse_post_order()

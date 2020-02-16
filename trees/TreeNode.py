class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if value == self.data:
            return

        if value < self.data:
            if self.left_child is None:
                self.left_child = TreeNode(value)
            else:
                self.left_child.insert(value)
        else:
            if self.right_child is None:
                self.right_child = TreeNode(value)
            else:
                self.right_child.insert(value)

    def get(self, value):
        if value == self.data:
            return self

        if value < self.data:
            if self.left_child is not None:
                return self.left_child.get(value)
        else:
            if self.right_child is not None:
                return self.right_child.get(value)

        return

    def min(self):
        if self.left_child is None:
            return self.data
        else:
            return self.left_child.min()

    def max(self):
        if self.right_child is None:
            return self.data
        else:
            return self.right_child.max()

    def traverse_in_order(self):
        if self.left_child is not None:
            self.left_child.traverse_in_order()

        print(self.data, end=", ")

        if self.right_child is not None:
            self.right_child.traverse_in_order()

    def traverse_pre_order(self):
        print(self.data, end=", ")

        if self.left_child is not None:
            self.left_child.traverse_pre_order()

        if self.right_child is not None:
            self.right_child.traverse_pre_order()

    def traverse_post_order(self):
        if self.right_child is not None:
            self.right_child.traverse_post_order()

        if self.left_child is not None:
            self.left_child.traverse_post_order()

        print(self.data, end=", ")

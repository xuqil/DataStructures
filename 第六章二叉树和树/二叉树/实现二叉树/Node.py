class Node:
    """
    二叉树
    """
    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_left(self, node):
        self._left = node

    def get_left(self):
        return self._left

    def set_right(self, node):
        self._right = node

    def get_right(self):
        return self._right


# if __name__ == '__main__':
#     root_node = Node('a')
#     left_node = Node('b')
#     right_node = Node('c')
#
#     root_node.set_left(left_node)
#     root_node.set_right(right_node)
#     print(root_node.get_data(), root_node.get_left().get_data(), root_node.get_right().get_data())
#     print(root_node.get_right())




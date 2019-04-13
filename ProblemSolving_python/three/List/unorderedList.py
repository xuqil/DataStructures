from ProblemSolving_python.three.List.node import Node


class UnorderedList:
    """
    链表头
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp


mylist = UnorderedList()
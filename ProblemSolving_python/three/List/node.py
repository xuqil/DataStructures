class Node:
    """
    实现链表节点
    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext


if __name__ == '__main__':
    temp = Node(93)
    print(temp.get_data())

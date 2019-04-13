class Queue:
    """
    使用列表实现队列
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        是否为空
        :return:
        """
        return self.items == []

    def enqueue(self, item):
        """
        入队
        :param item:
        :return:
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        出队
        :return:
        """
        return self.items.pop()

    def size(self):
        """
        队列大小
        :return:
        """
        return len(self.items)


if __name__ == '__main__':
    q = Queue()

    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.is_empty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())

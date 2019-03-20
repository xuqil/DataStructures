from 第三章线性表.链接表.单链表.循环单链表 import LClist


class Josephus(LClist):
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        LClist.__init__(self)
        for i in range(n):
            self.append(i + 1)
        self.turn(k - 1)
        while not self.is_empty():
            self.turn(m - 2)
            print(self.pop(), end=("\n" if self.is_empty() else ', '))


Josephus(10, 2, 7)
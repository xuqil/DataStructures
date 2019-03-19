from 第三章线性表.链接表.test3 import LNode
from 第三章线性表.链接表.test4 import LList
from random import randint


class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._head is None:  # 是空表
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next


mlist1 = LList1()
mlist1.prepend(99)
for i in range(11, 20):
    mlist1.append(randint(1, 20))

for x in mlist1.elements():
    print(x)

# for x in mlist1.filter(lambda y: y % 2 == 0):
#     print(x)

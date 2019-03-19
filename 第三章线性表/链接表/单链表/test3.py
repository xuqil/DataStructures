# 单链表类的实现
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


llist1 = LNode(1)
p = llist1

for i in range(2, 11):
    p.next = LNode(i)
    p = p.next

p = llist1
while p is not None:
    print(p.elem)
    p = p.next


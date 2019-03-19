class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        # 删除表头节点
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        # 后端操作
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        # 删除最后节点
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        # 表的遍历
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
            print('')

    def for_each(self, proc):
        # 表的遍历
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        # 迭代器
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        # 生成器查找
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q._next = p
            p = q
        self._head = p

    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next  # 从首节点之后开始处理
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:  # 跳过小元素
                p = p.next
            while p is not crt:  # 倒换大元素，完成元素插入的工作
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x  # 回填最后一个元素
            crt = crt.next

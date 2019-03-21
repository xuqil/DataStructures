class Stackunderflow(ValueError):
    # 栈下溢
    pass


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack:
    #  链表实现栈
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise Stackunderflow("in LStack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise Stackunderflow("is LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem



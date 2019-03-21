class Stackunderflow(ValueError):
    # 栈下溢
    pass


class SStack:
    # 顺序表实现栈
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise Stackunderflow("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise Stackunderflow("in SStack.pop()")
        return self._elems.pop()


# st1 = SStack()
# st1.push(3)
# st1.push(5)
# while not st1.is_empty():
#     print(st1.pop())


st1 = SStack()
for x in [1, 3, 5, 7, 9]:
    st1.push(x)
list2 = []
while not st1.is_empty():
    list2.append(st1.pop())
print(list2)
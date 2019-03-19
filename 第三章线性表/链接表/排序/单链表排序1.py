class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


def list_sort1(lst):
    p = lst
    if p is None:
        return
    crt = p.next
    while crt is not None:
        x = crt.elem
        while p is not crt and p.elem <= x:
            p = p.next
        while p is not crt:
            y = p.elem
            p.elem = x
            x = y
            p = p.next
        crt.elem = x
        crt = crt.next
    # while lst is not None:
    #     print(lst.elem)
    #     lst = lst.next
    return lst


lst = list_sort1(LNode(3, LNode(2, LNode(5, LNode(4, None)))))

while lst is not None:
    print(lst.elem)
    lst = lst.next

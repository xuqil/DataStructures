# 扫描、定位和遍历
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


head = LNode(None)
pre = LNode(1)
pre.next = head.next
head = pre  # 表头指向表首

# 在表首端插入元素
q = LNode(2)
q.next = pre.next
pre.next = q  # 表首的next指向下一个节点元素

print(head.elem)
print(pre.elem)
print(pre.next.elem)
print("="*60)

# 在其他位置插入元素
p = LNode(3)
p.next = pre.next
pre.next = p

# 按下表定位
h = head
while h is not None:
    print(h.elem)
    h = h.next

print("="*60)

# 按元素定位
pred = [1, 4, 5, 6, 7]
h = head
while h is not None and not pred[h.elem]:
    h = h.next
    print(h.elem)


# 求表长度
def length(head):
    h, n = head, 0
    while h is not None:
        n += 1
        h = h.next
    return n


print(length(head))


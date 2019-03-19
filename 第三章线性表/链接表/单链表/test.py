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

# 在其他位置插入元素
p = LNode(3)
p.next = pre.next
pre.next = p

print("="*60)
print(pre.next.elem)  # 原本是2，现在是3
print(p.elem)
print(p.next.elem)
print(q.elem)

# 删除表首
head = head.next

# 一般情况下的元素删除
pre.next = pre.next.next
print("="*60)
print(pre.next.elem)  # 原本是3，现在是2

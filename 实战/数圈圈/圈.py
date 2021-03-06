class ListNode(object):
    def __init__(self, x):
        self.x = x
        self.next = None


for _ in range(int(input())):
    num = int(input())
    head = ListNode(1)
    temp = head
    for i in range(2, num + 1):
        temp.next = ListNode(i)
        temp = temp.next
    temp.next = head
    temp = head
    res = []
    while temp.x != temp.next.x:
        print('temp.x:', temp.x)
        temp = temp.next
        res.append(temp.next.x)
        temp.next = temp.next.next
        temp = temp.next
    res.append(temp.x)
    print(' '.join(map(str, res)))

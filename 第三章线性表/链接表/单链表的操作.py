#链表节点结构实现  私有属性_pro_item是指向下个节点的指针，_item为此节点的值
class Node:

    def __init__(self, item=None, pos_item=None):
        self._item = item
        self._next = pos_item

    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出item
        '''
        return str(self._item)


class Chain:
    # 单链表实现
    def __init__(self):
        self._head = None
        self.length = 0

    def isEmpty(self):
        # 判空
        return self.length == 0

    def append(self, item):
        # 链表结尾插入
        if isinstance(item, Node):
            node = item
        else:
            node = Node(item)

        if self._head is None:
            self._head = node
        else:
            be_node = self._head
            while be_node._next:
                be_node = be_node._next
            be_node._next = node
        self.length += 1

    def insert(self, index, item):
        # 插入数据
        if self.isEmpty():
            print('this chain table is empty')
            return

        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        in_node = Node(item)
        node = self._head
        count = 1

        while True:
            node = node._next
            count += 1
            if count == index:
                next_node = node._next
                node._next = in_node
                in_node._next = next_node
                self.length += 1
                return

    def delete(self,index):
        # 删除数据
        if self.isEmpty():
            print('this chain table is empty')
            return

        if index<0 or index >= self.length:
            print("error: out of index")
            return
        else:
            node = self._head
            count = 0
            while True:
                count += 1
                if index == count:
                    node._next = node._next._next
                    break
                node = node._next
        self.length -= 1

    def __repr__(self):
        if self.isEmpty():
            print("the chain table is empty")
            return
        nlist = ""
        node = self._head
        while node:
            nlist += node._item +''
            node = node._next
        return nlist


if __name__ == '__main__':
    chain = Chain()
    chain.append('A')
    chain.append('B')
    chain.append('C')
    chain.append('D')
    chain.append('E')
    chain.append('F')
    chain.append('G')
    chain.insert(4, 'p')
    chain.delete(3)
    print(chain, chain._head._item,chain.length)

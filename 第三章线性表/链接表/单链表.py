#链表结构实现  私有属性_pro_item是指向下个节点的指针，_item为此节点的值
class ChainDemo:
    def __init__(self, item=None, pos_item=None):
        self._item = item
        self._pos_item = pos_item


if __name__ == '__main__':
    chain = ChainDemo('A', (ChainDemo('B', ChainDemo('C', ChainDemo('D')))))
    while True:
        print(chain._item)
        if chain._pos_item is not None:
            chain = chain._pos_item
        else:
            break


from 第六章二叉树和树.二叉树.实现二叉树.Node import Node


def pro_order(tree):
    # 先根遍历
    if tree is None:
        return False
    print(tree._data)
    pro_order(tree._left)
    pro_order(tree._right)


def pos_order(tree):
    # 后根遍历
    if tree is None:
        return False
    pos_order(tree._left)
    pos_order(tree._right)
    print(tree._data)


def mid_order(tree):
    # 中根遍历
    if tree is None:
        return False
    mid_order(tree._left)
    print(tree._data)
    mid_order(tree._right)


def row_order(tree):
    # 层次遍历
    queue = list()
    queue.append(tree)
    while True:
        if queue == []:
            break
        print(queue[0]._data)
        first_tree = queue[0]
        if first_tree._left != None:
            queue.append(first_tree._left)
        if first_tree._right is not None:
            queue.append(first_tree._right)
        queue.remove(first_tree)


if __name__ == '__main__':

    tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))
    # pro_order(tree)
    # mid_order(tree)
    # pos_order(tree)
    row_order(tree)

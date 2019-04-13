from ProblemSolving_python.three.Queue.deque import Deque


def palchecker(aString):
    """
    回文词判断
    :param aString:
    :return:
    """
    chardeque = Deque()
    for ch in aString:
        chardeque.add_rear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()
        if last != first:
            stillEqual = False
    return stillEqual


print(palchecker("adada"))

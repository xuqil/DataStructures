from ProblemSolving_python.three.Queue.queue import Queue


def hot_potato(namelist, num):
    """
    数圈圈
    从第一个开始，每经过num将第num个删除，然后重新开始数
    :param namelist:
    :param num:
    :return:
    """
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            if i == num - 1:
                simqueue.dequeue()
                continue
            a = simqueue.dequeue()
            simqueue.enqueue(a)
    return simqueue.dequeue()


print(hot_potato([1, 2, 3, 4, 5, 6], 4))
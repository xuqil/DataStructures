from ProblemSolving_python.three.Queue.queue import Queue


def hot_potato(namelist, num):
    """
    每经过num次队首的人就离队
    :param namelist:
    :param num:
    :return:
    """
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()
    return simqueue.dequeue()


print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))

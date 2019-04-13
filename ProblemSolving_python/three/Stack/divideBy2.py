from ProblemSolving_python.three.Stack.stack import Stack


def divideBy2(decNumber):
    """
    十进制转换成二进制
    :param decNumber:
    :return:
    """
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())

    return binString


print(divideBy2(10))

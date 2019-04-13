from ProblemSolving_python.three.Stack.stack import Stack


def divideBy2(decNumber, base):
    """
    十进制转换成二进制
    :param decNumber:
    :param base:
    :return:
    """
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binString = ''
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())

    return binString


print(divideBy2(10, 2))
print(divideBy2(10, 8))

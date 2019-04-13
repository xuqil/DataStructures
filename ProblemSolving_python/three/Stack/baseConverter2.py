from ProblemSolving_python.three.Stack.stack import Stack


def baseConverter(decNumber, base):
    """
    十进制转换成二进制
    :param decNumber:
    :param base:
    :return:
    """
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binString = ''
    while not remstack.is_empty():
        binString = binString + digits[remstack.pop()]

    return binString


print(baseConverter(10, 2))
print(baseConverter(10, 16))
print(baseConverter(10, 8))

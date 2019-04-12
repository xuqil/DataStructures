def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


from timeit import Timer
#
# t1 = Timer("test1()", "from __main__ import test1")
# print(t1.timeit(number=1000))
# t2 = Timer("test2()", "from __main__ import test2")
# print(t2.timeit(number=1000))
# t3 = Timer("test3()", "from __main__ import test3")
# print(t3.timeit(number=1000))
# t4 = Timer("test4()", "from __main__ import test4")
# print(t4.timeit(number=1000))

import timeit
print(timeit.timeit(stmt='list(range(2000000)).pop(0)', number=10))
print(timeit.timeit(stmt='list(range(2000000)).pop()', number=10))

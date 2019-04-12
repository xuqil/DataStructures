import time


def sum_of_n(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum, end - start


# for i in range(5):
#     print("Sum is %d required %10.7f seconds" % sum_of_n(10000))


def sum_of_n_3(n):
    return (n*(n+1))/2


for i in range(5):
    sum_of_n(i)

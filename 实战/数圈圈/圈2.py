def josephus_A(n, k, m):
    """
    :param n: n个人围成一个圈
    :param k: 从第k个人开始数
    :param m: 数到第m个人时，这个人出局
    :return: 胜出的最后一个人
    """
    people = list(range(1, n + 1))
    i = k - 1
    li = []
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                li.append(people[i])
                people[i] = 0
            i = (i + 1) % n  # 当数到第n个人时，然后返回第0个人开始重新数
    return li[n-1]


a = josephus_A(10, 2, 7)
print(a)

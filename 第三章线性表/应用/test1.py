def josephus_A(n, k, m):
    people = list(range(1, n + 1))
    i = k - 1
    # for num in range(n-1):
    for num in range(n):
        # print("第%s次" % num)
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            # print("i:", i, " n:", n)
            i = (i + 1) % n  # 当数到第n个人时，然后返回第0个人开始重新数
        if num < n - 1:
            print(", ", end="")
        else:
            print("")
        # print("最后一个人：", people)
    return


josephus_A(10, 2, 7)
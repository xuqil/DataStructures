def josephus_L(n, k, m):
    people = list(range(1, n + 1))
    num, i = n, k - 1
    li = []
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        li.append(people.pop(i))
    return li[n - 1]


print(josephus_L(10, 2, 7))

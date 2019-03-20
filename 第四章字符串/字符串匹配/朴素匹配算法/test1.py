def naive_matching(t, p):
    # 时间复杂度O(t*p)
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if p[i] == t[j]:  # 找到匹配
            i, j = i + 1, j + 1
        else:  # 字符不同，考虑下一个位置
            i, j = 0, j - i + 1
    if i == m:  # 找到匹配，返回开始下标
        return j - i
    return -1  # 无匹配，返回特殊值


print(naive_matching('hihaohello', 'hello'))

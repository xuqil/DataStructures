def matching_KMP(t, p, pnext):
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            i = pnext[i]
        if i == m:
            return j - 1
        return -1


def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m  # 初始数组元素全部为-1
    while i < m - 1:  # 生成一个pnext元素值
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k  # 设置pnext元素
        else:
            k = pnext[k]  # 退到更短相同前缀
    return pnext


print(gen_pnext("abbcabcaabbcaa"))
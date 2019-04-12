def gcd(m, n):
    # 欧里几何算法
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


print(gcd(2, 55))

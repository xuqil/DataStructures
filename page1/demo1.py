# 牛顿迭代法求平方根
def sqrt(x):
    y = 1.0
    while abs(y * y - x) > 1e-6:
        y = (y + x/y)/2
    return y


print(str(sqrt(9)))
print(1.0*1.0)

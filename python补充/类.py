class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        # 使用该方法，那么下面print(myfraction)直接打印实例输出的是return的内容，而不再是地址
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        # 添加该方法，使得实例可以使用“+”
        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        # 深比较
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum


def gcd(m, n):
    # 欧里几何算法
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


myfraction = Fraction(3, 5)
print(myfraction)
myfraction.show()

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)

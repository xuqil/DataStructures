from 第五章栈和队列.栈.zhan1 import SStack


def norec_fact(n):
    res = 1
    st = SStack()
    while n > 1:
        st.push(n)
        n -= 1
    while not st.is_empty():
        res *= st.pop()
    return res


print(norec_fact(5))


def fact(n):
    # 递归方法
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def make_sum(a, b):
    return ('+', a, b)


def make_prod(a, b):
    return ('*', a, b)


def make_diff(a, b):
    return ('-', a, b)


def make_div(a, b):
    return ('/', a, b)


def is_basic(a):
    return not isinstance(a, tuple)


def is_number(x):
    return (isinstance(x, int) or isinstance(x, float) or isinstance(x, complex))


def eval_exp(e):
    if is_basic(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    elif op == '-':
        return eval_diff(a, b)
    elif op == '*':
        return eval_prof(a, b)
    elif op == '/':
        return eval_div(a, b)
    else:
        raise ValueError("Unknown operator:", op)


def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a + b
    if is_number(a) and b == 0:
        return a
    if is_number(b) and a == 0:
        return b
    return make_sum(a, b)


def eval_div(a, b):
    if is_number(a) and is_number(b):
        return a / b
    if is_number(a) and a == 0:
        return 0
    if is_number(b) and b == 1:
        return a
    if is_number(b) and b == 0:
        raise ZeroDivisionError
    return make_div(a, b)


def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a - b
    if is_number(a) and b == 0:
        return a
    if is_number(b) and a == 0:
        return -b
    return make_diff(a, b)


def eval_prof(a, b):
    if is_number(a) and is_number(b):
        return a * b
    if is_number(a) and b == 0:
        return 0
    if is_number(b) and a == 0:
        return 0
    return make_prod(a, b)

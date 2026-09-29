def f():
    print(1)

print(2)
f()

def f1(x):
    """
    计算平方与两倍
    :param x: 给定值
    :return: 平方，两倍
    """
    return x ** 2, x * 2

print(f1(4))
# help(f1)

def f2(x):
    if x == 0:
        return

    print(f"f2({x})")
    f3(x - 1)

def f3(x):
    if (x == 0):
        return

    print(f"f3({x})")
    f2(x - 1)

f2(5)

num = 1
def f4():
    global num
    print(num)

    num = 100
    print(num)

f4()
print(num)

def f5(x, y):
    return y, x

print(f5(y = 10, x = 5))

def f6(x, y = "a"):
    return y, x

print(f6(10))
print(f6(10, "5"))

def f7(*args):
    return min(args), max(args), round(sum(args) / len(args), 1)

print(f7(1, 2, 3, 4))

def f8(**kwargs):
    print(kwargs)

f8(a = "a", b = 3)

def f9(x, f):
    return f(x)

print(f9(5, f1))
print(f9(5, lambda x: x * 2))

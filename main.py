eps = 10 ** -6


def func(x):
    return x ** 4 - x


def dih(a, b):
    d = abs(a - b)
    iter = 0
    z = 0
    while (d > eps):
        d = abs(a - b)
        f_left = func(a + d * 0.25)
        f_rigth = func(a + d * 0.75)
        if f_left > f_rigth:
            a = a
            b = a + 0.5 * d
            z = f_left
        else:
            a = a + 0.5 * d
            b = b
            z = f_rigth
        # print(f"Iteration: {iter}")
        iter += 1
    print(f"Quantity of iteration: {iter}")
    print("Value of the target function: {zz:5.8f}".format(zz=z))


def zol(a, b):
    d = abs(a - b)
    iter = 0
    z = 0
    while (d > eps):
        d = abs(a - b)
        dd = (d * 5 / 8)
        f_left = func(a + dd * 5 / 8)
        f_rigth = func(a + dd + dd * 5 / 8)
        if f_left > f_rigth:
            a = a
            b = a + 5 / 8 * d
            z = f_left
        else:
            a = a + 5 / 8 * d
            b = b
            z = f_rigth
        # print(f"Iteration: {iter}")
        iter += 1
    print(f"Quantity of iteration: {iter}")
    print("Value of the target function: {zz:5.8f}".format(zz=z))


def m_fib(a, b):
    d = abs(a - b)
    iter = 0
    z = 0
    prev_fib = 1
    fib = 2
    while (d > eps):
        d = abs(a - b)
        t = 1 / fib
        dd = (d * t)
        f_left = func(a + dd * t)
        f_rigth = func(a + dd + dd * t)
        if f_left > f_rigth:
            a = a
            b = a + t * d
            z = f_left
        else:
            a = a + t * d
            b = b
            z = f_rigth
        # print(f"Iteration: {iter}")
        iter += 1
        tmp = fib
        fib = prev_fib + fib
        prev_fib = tmp
        # print(fib)
    print(f"Quantity of iteration: {iter}")
    print("Value of the target function: {zz:5.16f}".format(zz=z))


if __name__ == '__main__':
    a = 0
    b = 1
    print("Метод дихотомии:")
    dih(a, b)
    print("Метод золотого сечения:")
    zol(a, b)
    print("Метод чисел Фибоначи:")
    m_fib(a, b)

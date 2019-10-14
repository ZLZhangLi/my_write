# n = int(input())
n = 10
def func(a):
    if a < 1e-5:
        return 0
    last = a
    c = a / 2
    while abs(c - last) > 1e-5:
        last = c
        c = (c + a / c) / 2
    return c
res = func(n)
print(format(res,'.4f'))
print('{:.2f}'.format(res))
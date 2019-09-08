#n = int(input())
def fib_loop(f,n):
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        f.append(f[i - 1] + f[i - 2])
    return f

m = []
print(fib_loop(m,5))
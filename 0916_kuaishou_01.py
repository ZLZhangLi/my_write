n = int(input())
count = 0
def f(n):
    result = []
    i = 2
    while n > 1:
        if n % i == 0:
            n /= i
            result.append(str(i))
            i -= 1
        i += 1
    return len(result)

if __name__ == '__main__':
    for i in range(2, n+1):
        count += f(i)
    print(count)
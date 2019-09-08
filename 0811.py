n = int(input())
a = list(map(int, input().strip().split()))
a.sort()
sum = 0
avg = 0
dd = []

for i in range(len(a)-2):
    avg = (a[i]+a[i+1]+a[i+2]) / 3
    d = 1.0 * ((a[i] - avg) ** 2 + (a[i+1] - avg) ** 2 + (a[i+2] - avg) ** 2) / 3
    dd.append(d)
avg = (a[-3] + a[-2] + a[-1]) / 3
d = 1.0 * ((a[-3] - avg) ** 2 + (a[-2] - avg) ** 2 + (a[i-1] - avg) ** 2) / 3
dd.append(d)
print (round(min(dd),2))
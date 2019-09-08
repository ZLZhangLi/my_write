s1 = list(input().strip().split(','))
s1.sort()
s2 = []
for i in range(len(s1)):
    a = s1[-i-1]
    i += 1
    s2.append(a)
for i in s2:
    print(i,end=',')
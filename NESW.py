Num = int(input())
s = input()
r = 0
l = 0
total = 0
a = s[1]
for i in range(Num):
    if s[i] == 'L':
        total -= 1
    elif s[i] == 'R':
        total += 1

if total % 4 == 0:
    print('N')
elif total % 4 == 1:
    print('E')
elif total % 4 == 2:
    print('S')
elif total % 4 == 3:
    print('W')
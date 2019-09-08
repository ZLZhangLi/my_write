s = 'We Are Happy'

n = s.split(' ')
ss = n[0]
for i in range(len(n)):
    if i < len(n) - 1:
        ss += '%20' + n[i + 1]
    else:
        continue
print(ss)
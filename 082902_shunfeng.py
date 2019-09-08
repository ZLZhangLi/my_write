dis = int(input())
min_len = int(input())
max_len = int(input())
s1 = raw_input()
s2 = raw_input()
str1 = s1.split(',')
str2 = s2.split(',')
print(str1)
print(str2)
str3 = str1 + str2
print(str3)
res = 0
for index in xrange(len(str3)):
    if len(str3[index]) >= min_len and len(str3[index]) <= max_len:
        res += 1
print(res)
n,s = list(map(int, input().strip().split()))
# n = 10
# a= 3
ss = list(range(1,s + 1))
m = 0
# for i in range(len(s)):
#     for j in range(1,len(s)- i + 1):
#         a = sum(s[i:i+j])
# for j in range(len(n)):
#     for i in range(len(ss)):
#         a = sum(ss[i:i+n])
#         if a == s:
#             m +=1

for i in range(len(ss)):
    for j in range(i + 1,len(ss)):
        for k in range(j + 1,len(ss)):
            a = ss[i]+ss[j]+ss[k]
            if a == s:
                m +=1
print (m)


# d = [s[i:i+j] for i in range(len(s)) for j in range(1,len(s)- i + 1) if sum(s[i:i+j])==n]
# print (d)
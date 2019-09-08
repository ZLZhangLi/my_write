s = input()
count ={}
for i in set(s):
    count[i]=s.count(i)
#print(count)
a = count.values()
max_value=max(count.values())
print(max_value)

# n,N = list((input().split(';')))
# n = list(map(int,n.split(',')))
# N = int(N)
# str1= sorted([i for i in n if (i%2) == 0],reverse=True)
# str2 = sorted([j for j in n if (j%2) == 1],reverse=True)
# res = str1 + str2
# print(','.join([str(num) for num in res[:N]]))
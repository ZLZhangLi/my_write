#输入两个数字，N和M
n,m = list(map(int,input().strip().split()))

#输入一个列表M = []
m = list(map(int,input().strip().split()))

#按N依次读入每行数据到列表中
while(i < n):
    xy.append(list(map(int,input().strip().split())))
    i += 1
for i in range(n):
    xy.append(list(map(int, input().strip().split())))

#循环输入，直到空行结束
import sys
while True:
    line = sys.stdin.readline()
    if line == '\n':
        break
    i,j = list(map(int,line.split()))

#按空格输出
e = [4,4,3,3,2]
for i in e:
    print(i, end = ' ')
#按分行输出
e = [4,4,3,3,2]
for i in e:
    print(i)

#列表转字符串
# 一、list转字符串
#
# 命令：''.join(list)
# 其中，引号中是字符之间的分割符，如“,”，“;”，“\t”等等
# 如：
list = [1, 2, 3, 4, 5]
a = ''.join(list) #结果即为：12345
a = '12345'
b = ','.join(list) #结果即为：1,2,3,4,5
b = '1,2,3,4,5'

#字符串转list

print (list('12345'))
output = ['1', '2', '3', '4', '5']
#输出： ['1', '2', '3', '4', '5']
print (list(map(int, '12345')))
output = [1,2,3,4,5]

str2 = "123 sjhid dhi"
list2 = str2.split() #or list2 = str2.split(" ")
print (list2)
output = ['123', 'sjhid', 'dhi']

str3 = "www.google.com"
list3 = str3.split(".")
print (list3)
output = ['www', 'google', 'com']

#测试时间
import time
t1 = time.clock()
t2 = time.clock()
print(t2 - t1)
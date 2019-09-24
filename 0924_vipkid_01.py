num = int(input())
ss = ''
count = 0
def binary2(data,sss,base):
    while data > 0:
        data,yushu = data // base,data % base
        sss += str(yushu)
    return sss[::-1]

res = binary2(num,ss,2)
for i in res:
    if i == '1':
        count += 1

print(count)
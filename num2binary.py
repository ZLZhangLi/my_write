num = int(input())
m_base = int(input())
#num = 6
ss = ''
def binary(data,sss,base):
    if data // base == 0:
        sss += str(data%base)
        return sss[::-1]
    else:
        sss += str(data % base)
        #binary(int(data / 2), sss)
        return(binary(data // base, sss,base))
    #return sss[::-1]
#binary = lambda n: '' if n==0 else binary(int(n/2)) + str(n%2)
def binary2(data,sss,base):
    while data > 0:
        data,yushu = data // base,data % base
        sss += str(yushu)
    return sss[::-1]
#res = binary(num,ss, m_base)
res = binary2(num,ss, m_base)
print(res)
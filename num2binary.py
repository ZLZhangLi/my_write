num = int(input())
#num = 6
ss = ''
def binary(data,sss):
    if int(data / 2) == 0:
        sss += str(data%2)
        return sss[::-1]
    else:
        sss += str(data % 2)
        #binary(int(data / 2), sss)
        return(binary(int(data / 2), sss))
    #return sss[::-1]
#binary = lambda n: '' if n==0 else binary(int(n/2)) + str(n%2)
res = binary(num,ss)
print(res)
import math
from fractions import Fraction
def comb(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))

n,p,q = list(map(int,input().strip().split()))
res = 0
for i in range(p,n-q+1):
    res += comb(n,i)
m = Fraction(1,res)
e= 0
for i in range(p,n-q+1):
    e += i * comb(n, i) * m
print(e)
print(int((e.numerator + 1000000007) / e.denominator))


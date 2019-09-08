import sys
def longestCommonPrefix(str1,str2):
    res = 0
    for i in range(min(len(str1),len(str2))):
        if str1[i] == str2[i]:
            res += 1
        else:
            break
    return res
if __name__ == '__main__':
    n = int(input())
    m,k = [],[]
    num = []
    for i in range(n):
        m.append(input().strip())
    while True:
        line = sys.stdin.readline()
        if line == '\n':
            break
        i,j = list(map(int,line.split()))
        if i < len(m) + 1 and j < len(m) + 1:
            res = longestCommonPrefix(m[i-1],m[j-1])
        else:
            res = ''
        num.append(res)

        #print(res)
    for i in num:
        print(i)


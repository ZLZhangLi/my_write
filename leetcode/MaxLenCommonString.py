str1 = input().strip()
str2 = input().strip()
N = len(str1)
M = len(str2)

def LCS(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1] + 1
            else:
                res[i][j] = max(res[i-1][j],res[i][j-1])
    return res[-1][-1]

if __name__ == '__main__':
    res = LCS(str1,str2)
    print(len(res))



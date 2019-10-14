data = input().split('<ctrip>')
print(data[0])
print(data[1])

def dis(s1, s2):

    len_str1 = len(s1) + 1
    len_str2 = len(s2) + 1


    matrix = [[0] * (len_str2) for i in range(len_str1)]

    for i in range(len_str1):
        for j in range(len_str2):
            if i == 0 and j == 0:
                matrix[i][j] = 0

            elif i == 0 and j > 0:
                matrix[0][j] = j
            elif i > 0 and j == 0:
                matrix[i][0] = i

            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1] + 1, matrix[i - 1][j] + 1)
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j] + 1)
    return matrix[len_str1 - 1][len_str2 - 1]

print(dis(data[0],data[1]))
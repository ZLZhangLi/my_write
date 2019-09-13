#m_str = list(input().strip().split(','))
#res = 0
# for i in range(len(m_str)):
#     if len(m_str[i]) > 1:
#         if m_str[i].isdigit():
#             sum = int(m_str[i][0]) + int(m_str[i][-1])
#             if sum > 8:
#                 res += 1
# print(res)
count = 0
for i in range(1,10001):
    if i % 3 == 0 and i % 7 ==0 and i % 11 == 0:
        count += 1
print(10000-count)
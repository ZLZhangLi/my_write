# m_str = input().strip()
# m_left = 0
# m_right = 0
# for i in range(len(m_str)):
#     if m_str[i] == '[':
#         m_left += 1
#     elif m_str[i] == ']':
#         m_right += 1
#     else:
#         continue
# print(abs(m_left - m_right))

m_str = input().strip()
stack = []
for i in range(len(m_str)):
    if stack:
        if m_str[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(m_str[i])
        if m_str[i] == '[':
            stack.append(m_str[i])
    else:
        stack.append(m_str[i])

print(len(stack))
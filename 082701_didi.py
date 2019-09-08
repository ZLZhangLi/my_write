n = int(input())
eq = list(input().strip().split())
nums = []
symbol = []
res = ''
for i in range(int(len(eq)/2)):
    nums.append(int(eq[2*i]))
    symbol.append(eq[2 * i + 1])
nums.append(int(eq[-1]))
for j in range(len(nums)):
    for i in range(len(symbol) - j):
        if nums[i] > nums[i + 1]:
            if symbol[i] == '+':
                if i == len(symbol) - 1:
                    if symbol[i - 1] == '+':
                        nums[i + 1], nums[i] = nums[i], nums[i + 1]
                elif i > 0:
                    if symbol[i - 1] == '+' and (symbol[i + 1] == '+' or symbol[i + 1] == '-'):
                    #if symbol[i + 1] == '+' or symbol[i + 1] == '-' and symbol[i - 1] == '+':
                        nums[i + 1], nums[i] = nums[i], nums[i + 1]
                elif i == 0:
                    if symbol[i + 1] == '+' or symbol[i + 1] == '-':
                        nums[i + 1], nums[i] = nums[i], nums[i + 1]
            elif symbol[i] == '-':
                if i == len(symbol) - 1:
                    if symbol[i - 1] == '-':
                        nums[i + 1], nums[i] = nums[i], nums[i + 1]
                elif i > 0:
                    if symbol[i - 1] == '-' and (symbol[i + 1] == '-' or symbol[i + 1] == '+'):
                        nums[i + 1], nums[i] = nums[i], nums[i + 1]
                elif i == 0:
                    continue
            elif symbol[i] == '*':
                if i > 0:
                    if symbol[i - 1] != '/':
                        nums[i + 1], nums[i] = nums[i], nums[i + 1]
                elif i == 0:
                    nums[i + 1], nums[i] = nums[i], nums[i + 1]
            elif symbol[i] == '/':
                if i > 0:
                    if symbol[i - 1] == '/':
                        nums[i + 1], nums[i] = nums[i], nums[i + 1]
                elif i == 0:
                    continue

for i in range(len(symbol)):
    res += ' ' + str(nums[i])
    res += ' ' + str(symbol[i])
res += ' ' + str(nums[-1])
print(res.strip())
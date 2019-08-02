import os
N = int(input())
input_list = list(map(int,input().strip().split()))
Num0 = 0
Num1 = 0
Num2 = 0
Num3 = 0
temp = []
total = 1

for index in range(len(input_list)):
    if N != len(input_list) or input_list[index] < 0:
        print (0)
        break
    else:
        if input_list[index] == 0:
            if index == 0 && input_list[1] != 0:
                Num0 = input_list[index + 1]
                temp.append(Num0)
            elif index == 0 && input_list[1] == 0:
                
            elif index == 1:
                Num1 = 1
                temp.append(Num1)
            elif index < len(input_list) - 1:
                Num2 = input_list[index - 1] - input_list[index + 1] + 1
                temp.append(Num2)
            else:
                Num3 = input_list[index - 1]
                temp.append(Num3)
for i in temp:
    total = total * i

print (total)
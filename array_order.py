array = [1,2,3,4,5,6]
a = []
b = []
# for index in range(len(array)):
#     if 2 * index < len(array):
#         a.append(array[2 * index + 1])
#         b.append(array[2 * index])
#         c = a + b
#     else:
#         break
# print c
# for index in range(len(array)):
#     if array[index] % 2 == 1:
#         a.append(array[index])
#     else:
#         b.append(array[index])
# print a+b
c = (2 * x - 1 for x in range(1,101))
print type(c)
#print c[0]
print next(c)
print next(c)
print next(c)

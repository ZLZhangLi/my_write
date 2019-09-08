#滑窗法 最大不重复子字符串
# set()容器 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
# x = set('runoob')
# y = set('google')
# x, y
# (set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
# x & y         # 交集
# set(['o'])
# x | y         # 并集
# set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
# x - y         # 差集
# set(['r', 'b', 'u', 'n'])

s = input().strip()
#s = 'abcabcbb'
if not s: print(0)
left = 0
lookup = set()
n = len(s)
max_len = 0
cur_len = 0
for i in range(n):
    cur_len += 1
    while s[i] in lookup:
        lookup.remove(s[left])
        left += 1
        cur_len -= 1
    if cur_len > max_len:max_len = cur_len
    lookup.add(s[i])
print (max_len)

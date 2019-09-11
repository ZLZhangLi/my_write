a,b,c = list(input().strip().split())
a_list = c.split(a)
print(len(a_list))
for i in range(len(a_list)):
    m_key,m_value = a_list[i].split(b)
    print(str(m_key) + ' ' + str(m_value))

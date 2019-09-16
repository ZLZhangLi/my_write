s = input().strip()
m_index = []
count = 0
Mod = 10 ** 9 + 7

def replace_char(string,char,index):
     string = list(string)
     string[index] = char
     return ''.join(string)

def fun1(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '?':
            m_index.append(i)

    if len(m_index) == 0:
        if int(s) % 13 == 5:
            count += 1
    elif len(m_index) == 1:
        for i in range(10):
            s = replace_char(s, str(i), m_index[0])
            if int(s) % 13 == 5:
                count += 1
    elif len(m_index) == 2:
        for i in range(10):
            s = replace_char(s, str(i), m_index[0])
            for j in range(10):
                s = replace_char(s, str(j) ,m_index[1])
                if int(s) % 13 == 5:
                    count += 1
    elif len(m_index) == 3:
        for i in range(10):
            s = replace_char(s, str(i), m_index[0])
            for j in range(10):
                s = replace_char(s, str(j), m_index[1])
                for k in range(10):
                    s = replace_char(s, str(k), m_index[2])
                    if int(s) % 13 == 5:
                        # print(int(s))
                        count += 1
    elif len(m_index) == 4:
        for i in range(10):
            s = replace_char(s, str(i), m_index[0])
            for j in range(10):
                s = replace_char(s, str(j), m_index[1])
                for k in range(10):
                    s = replace_char(s, str(k), m_index[2])
                    for p in range(10):
                        s = replace_char(s, str(p), m_index[3])
                        if int(s) % 13 == 5:
                            count += 1
    elif len(m_index) == 5:
        for i in range(10):
            s = replace_char(s, str(i), m_index[0])
            for j in range(10):
                s = replace_char(s, str(j), m_index[1])
                for k in range(10):
                    s = replace_char(s, str(k), m_index[2])
                    for p in range(10):
                        s = replace_char(s, str(p), m_index[3])
                        for q in range(10):
                            s = replace_char(s, str(q), m_index[4])
                            if int(s) % 13 == 5:
                                count += 1
    return count
def fun2(string1,string2):
    count = 0
    for i in range(len(string1)):
        if string1[i] == '?':
            string1 = replace_char(string1,'9',i)
    for i in range(len(string2)):
        if string2[i] == '?':
            string2 = replace_char(string2, '0', i)
    # print(int(string1))
    # print(int(string2))
    for i in range(int(string2),int(string1)+1):
        if i % 13 == 5:
            count += 1
            print(i)
    return count

res1 = fun1(s) % Mod
res2 = fun2(s,s) % Mod
print(res1)
print(res2)
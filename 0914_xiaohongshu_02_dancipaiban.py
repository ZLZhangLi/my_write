class Solution:
    def fullJustify(self, words, maxWidth):
        ans,temp,mark=[],[],0
        for _ in words:
            #这里的tricky我喜欢（自己想的），表示的是后续单词需要空格位
            mark+=len(_)+(mark !=0)
            if mark<=maxWidth:
                temp.append(_)
            else:
                temp_line=''
                space=maxWidth-sum([len(_) for _ in temp])
                if len(temp)==1:#只有一个时要左对齐
                    temp_line+=temp.pop()+' '*space
                else:
                    while temp!=[]:
                        if len(temp)==1:#这里写出来是避免0除，用try应该也可以
                            temp_line+=temp.pop()
                        else:
                            temp_line+=temp.pop(0)+' '*((space-1)//len(temp)+1)
                            #这里对空格的处理也比较数学化，不够编程性
                            space-=((space-1)//len(temp)+1)
                ans.append(temp_line)
                mark=len(_)
                temp.append(_)

        temp_line=' '.join(temp)
        temp_line+=' '*(maxWidth-len(temp_line))

        ans.append(temp_line)

        return ans

m = int(input())
m_list = list(input().strip().split())
a = Solution()
res = a.fullJustify(m_list,m)
for i in range(len(res)):
    ll = res[i].split()
    m_str = ''
    for j in range(len(ll)-1):
        m_str += ll[j] + ' '
    m_str += ll[-1]
    out_put = m_str.center(m, ' ')
    print(out_put)
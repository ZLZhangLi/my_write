# m = list(map(int,input().strip().split()))
def bubble_sort(alist):
    '''冒泡排序'''
    pass

def select_sort(alist):
    '''选择排序'''
    for i in range(len(alist) - 1):
        min_index = i
        for j in range(i + 1,len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]
    return alist

def insert_sort(alist):
    '''插入排序'''
    for i in range(1, len(alist)):
        for j in range(i-1, -1, -1):
            if alist[i] < alist[j]:
                alist[i],alist[j] = alist[j],alist[i]
            else:  #插入算法的优化，如果后面的值大于前面的有序序列的数，则退出循环。
                break
    return alist
def shell_sort():
    '''希尔排序'''
    pass

def quick_sort(alist):
    '''快速排序'''
    pass

if __name__ == '__main__':
    m = [1,4,3,5,11,6]
    print(m)
    # res = select_sort(m)
    # res = insert_sort(m)
    print(select_sort(m))
    print(insert_sort(m))
    # for i in res:
    #     print(i,end= ' ')
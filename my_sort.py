# m = list(map(int,input().strip().split()))
def bubble_sort(alist):
    '''冒泡排序'''
    isSort = True
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                isSort = False
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
        if isSort:
            break
    return alist

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

def merge_sort(alist):
    '''归并排序'''
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    #left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    #right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])
    left_pointer, right_pointer = 0, 0
    res = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            res.append(left_li[left_pointer])
            left_pointer += 1
        else:
            res.append(right_li[right_pointer])
            right_pointer += 1
    res += left_li[left_pointer:]
    res += right_li[right_pointer:]
    return res


def Quick_sort(alist):
    '''快速排序'''
    def get_index(arr,left,right):
        key = left
        while left < right:
            while left < right and arr[right] >= arr[key]:
                right -= 1
            while left < right and arr[left] <= arr[key]:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        arr[left], arr[key] = arr[key], arr[left]
        return left

    def quick_sort(arr, left, right):
        if left >= right:
            return
        mid = get_index(arr, left, right)
        quick_sort(arr, left, mid)
        quick_sort(arr, mid + 1, right)

    n = len(alist)
    if n <= 1:
        return alist
    quick_sort(alist,0,n-1)
    return alist

if __name__ == '__main__':
    m = [1,4,3,5,11,6]
    print(m)
    # res = select_sort(m)
    # res = insert_sort(m)
    print(select_sort(m))
    print(insert_sort(m))
    # for i in res:
    #     print(i,end= ' ')
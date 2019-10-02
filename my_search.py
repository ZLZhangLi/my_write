def binary_search1(alist,k):
    '''二分查找'''
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == k:
            return True
        elif alist[mid] > k:
            return binary_search1(alist[:mid],k)
        else:
            return binary_search1(alist[mid + 1:],k)
    return False

def binary_search2(alist,k):
    n = len(alist)
    left = 0
    right = n-1
    # mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        if alist[mid] == k:
            return True
        elif alist[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return False

if __name__ == "__main__":
    li = [17,20,26,31,44,54,55,77,93]
    # print(binary_search1(li,55))
    print(binary_search2(li,100))
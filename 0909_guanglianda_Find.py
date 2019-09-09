class Node(object):
    def __init__(self, value, next=0):
        self.value = value
        self.next = next
def createLink(n):
    root = Node(n[0])
    tmp = root
    for i in range(1, len(n)):
        tmp.next = Node(n[i])
        tmp = tmp.next
    return root

if __name__ == '__main__':
    data = list(map(int,input().strip().split()))
    m_linklist = createLink(data)
    print(is_palindrome1(m_linklist))

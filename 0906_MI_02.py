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
def is_palindrome1(head):

    if head == 0 or head.next == 0:
        return True
    p = head
    stack = []
    while p != 0:
        stack.append(p.value)
        p = p.next
    p = head
    while p != 0:
        if p.value != stack.pop():
            return False
        p = p.next
    return True
if __name__ == '__main__':
    data = list(map(int,input().strip().split()))
    m_linklist = createLink(data)
    print(is_palindrome1(m_linklist))

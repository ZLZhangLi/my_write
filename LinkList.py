#创建链表
class Node(object):
    def __init__(self, value, next=0):
        self.value = value
        self.next = next

def createLinkList(n):
    root = Node(n[0])
    tmp = root
    for i in range(1, len(n)):
        tmp.next = Node(n[i])
        tmp = tmp.next
    return root
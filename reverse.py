# a = ['zhangli','lizhang','hehe']
# for index , item in enumerate(a):
#     print (index, item)
#     print index, item
#
# print a[-2:-1]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
dummy = ListNode(0)
pHead = dummy
pHead1 = ListNode(1)
pHead2 = ListNode(2)
a = pHead.val
b = pHead1.val
c = pHead2.val
while pHead1 and pHead2:
    if pHead1.val >= pHead2.val:
        dummy.next = pHead2
        pHead2 = pHead2.next
    else:
        dummy.next = pHead1
        pHead1 = pHead1.next

    dummy = dummy.next

if pHead1:
    dummy.next = pHead1
elif pHead2:
    dummy.next = pHead2
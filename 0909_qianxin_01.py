class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def listcreattree(root, llist, i):

    if i < len(llist):
        if llist[i] == '#':
            return None
        else:
            root = TreeNode(llist[i])

            root.left = listcreattree(root.left, llist, 2 * i + 1)

            root.right = listcreattree(root.right, llist, 2 * i + 2)
            return root
    return root
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        p_val = p.val
        q_val = q.val

        node = root
        while node:

            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node.val


n = int(input())
m = list(map(int,input().strip().split()))
p,q = list(map(int,input().strip().split()))
res = listcreattree(None, m, 0)
p_node = TreeNode(p)
q_node = TreeNode(q)
a = Solution()
ans = a.lowestCommonAncestor(res,p_node,q_node)
print(ans)

import queue
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    def set_data(self, data):
        self.val = data
    def get_data(self):
        return self.val
    def set_left(self, node):
        self.left = node
    def get_left(self):
        return self.left
    def set_right(self, node):
        self.right = node
    def get_right(self):
        return self.right

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

class Solution():
    def Preorder_Traversal(self,root):
        '''前序遍历'''
        if not root:
            return []
        stack, res = [root],[]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res

    def Midorder_Traversal(self,root):
        '''中序遍历'''
        if not root:
            return []
        stack, res = [],[]
        node = root
        while stack or node: #从根节点开始，一直寻找它的左子树
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def Postorder_Traversal(self,root): # 堆栈实现后序遍历（非递归）
        '''后序遍历 非递归'''
        # 使用两个栈结构
        # 第一个栈进栈顺序：左节点->右节点->根节点
        # 第一个栈弹出顺序： 根节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
        # 第二个栈存储为第一个栈的每个弹出依次进栈
        # 最后第二个栈依次出栈
        if not root:
            return []
        node = root
        stack1,stack2,res = [node],[],[]
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            res.append(stack2.pop().val)
        return res

class Solution2():
    def Preorder_Traversal(self,root):
        res = []
        def dfs(node):
            if not node: return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

    def Midorder_Traversal(self,root):
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    def Postorder_Traversal(self,root):
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
class Solution3():
    '''层次遍历'''
    def bfs(self,root):
        '''广度优先'''
        if not root: return
        #队列，保存节点
        que = queue.Queue()
        que.put(root)
        res = []
        while not que.empty():
            curNode = que.get()
            res.append(curNode.val)
            if curNode.left:
                que.put(curNode.left)
            if curNode.right:
                que.put(curNode.right)
        return res
class Solution4():
    def dfs(self,root):
        '''深度优先'''
        if not root: return
        # 栈用来保存未访问节点
        stack = []
        # vals保存节点值，作为结果
        vals = []
        stack.append(root)

        while stack:
            # 拿出栈顶节点
            currentNode = stack.pop()
            vals.append(currentNode.val)
            # print(currentNode.val, end=' ')
            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)
        return vals

def TreeNums(root):
    if not root: return 0
    nums = TreeNums(root.left)
    nums += TreeNums(root.right)
    return nums + 1
def TreeHights(root):
    if not root: return 0
    ldepth = TreeHights(root.left)
    rdepth = TreeHights(root.right)
    return max(ldepth,rdepth) + 1

if __name__ == '__main__':
    # 实例化根节点
    root_node = TreeNode('a')
    # root_node.set_data('a')
    # 实例化左子节点
    left_node = TreeNode('b')
    # 实例化右子节点
    right_node = TreeNode('c')
    # 给根节点的左指针赋值，使其指向左子节点
    root_node.set_left(left_node)
    # 给根节点的右指针赋值，使其指向右子节点
    root_node.set_right(right_node)

    m_list = [1,2,3,4,5,6,7,8]
    m_root = listcreattree(None,m_list,0)
    print(m_root)
    print(m_root.get_data(), m_root.get_left().get_data(), m_root.get_right().get_data())
    a = Solution()
    print(a.Preorder_Traversal(m_root))
    print(a.Midorder_Traversal(m_root))
    print(a.Postorder_Traversal(m_root))
    b = Solution2()
    print(b.Preorder_Traversal(m_root))
    print(b.Midorder_Traversal(m_root))
    print(b.Postorder_Traversal(m_root))
    c = Solution3()
    print(c.bfs(m_root))
    d = Solution4()
    print(d.dfs(m_root))
    print(TreeHights(m_root))
    print(TreeNums(m_root))

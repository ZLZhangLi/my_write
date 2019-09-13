class TreeNode():
    def __init__(self,x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

def pro_order(tree):
    if tree == None:
        return False
    print(tree.val)
    pro_order(tree.left)
    pro_order(tree.right)

def mid_order(tree):
    if tree == None:
        return False
    mid_order(tree.left)
    print(tree.val)
    mid_order(tree.right)

def pos_order(tree):
    if tree == None:
        return False
    pos_order(tree.left)
    pos_order(tree.right)
    print(tree.val)

if __name__ == '__main__':

    m_tree = TreeNode('A',TreeNode('B',TreeNode('D'),TreeNode('E')),TreeNode('C',TreeNode('F'),TreeNode('G')))
    pro_order(m_tree)
    mid_order(m_tree)
    pos_order(m_tree)

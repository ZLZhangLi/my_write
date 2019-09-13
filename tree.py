# 实现树结构的类，树的节点有三个私有属性  左指针 右指针 自身的值
class TreeNode():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
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

    m_list = [1,2,3,4,5,6]
    m_root = listcreattree(None,m_list,0)
    print(m_root)
    print(root_node.get_data(), root_node.get_left().get_data(), root_node.get_right().get_data())

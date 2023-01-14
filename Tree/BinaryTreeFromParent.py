''' Given an array parent which represents  a  binary tree such that parent-child
relationship  is defined  by (parent[i],i) which means that parent of i is parent[i]
. the value  of the root node will be i if -1 is present at parent[i].'''

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTreeHelper(root, parent):
    if root is None:
        return

    first = None
    second = None

    f = 0
    for  i in range(len(parent)):
        if parent[i] == root.data and f==0:
            temp = BinaryTreeNode(i)
            first =temp
            f += 1
        elif parent[i] == root.data:
            temp = BinaryTreeNode(i)
            second = temp

    root.left = createTreeHelper(first, parent)
    root.right = createTreeHelper(second, parent)

    return root

def createTree(parent):
    # T --> O(N**2) and S --> O(H) H --> height of tree
    root = BinaryTreeNode(0)
    for i in range(len(parent)):
        if parent[i] == -1: 
            root.data = i
            break
    
    root = createTreeHelper(root, parent)
    return root
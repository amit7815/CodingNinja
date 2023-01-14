class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def verticalOrderTraversal(m, hd, root):
    if root is None:
        return

    try:
        m[hd].append(root.data)
    except:
        m[hd] = [root.data]

    verticalOrderTraversal(m, hd-1, root.left)
    verticalOrderTraversal(m, hd+1, root.right)


def printVerticalOrder(root):
    m = {}
    verticalOrderTraversal(m, 0, root)
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i, end='')
        print()




node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)
node7 = BinaryTreeNode(7)
node8 = BinaryTreeNode(8)
node9 = BinaryTreeNode(9)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9

printVerticalOrder(node1)

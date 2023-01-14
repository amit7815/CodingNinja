class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def helper(root, hDistance, level, visited):
    if root is None:
        return 

    if hDistance not in visited or visited[hDistance][1] > level:
        visited[hDistance] = [root.data, level]

    helper(root.left, hDistance-1, level+1, visited)

    helper(root.right, hDistance+1, level+1, visited)


def topView(root):
    ''' T -- O(N*logN)  S -- O(N) '''
    visited = {}
    helper(root, 0, 0, visited)
    ans = []
    for i in visited:
        ans.append(visited[i][0])

    print(ans)


node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)
node7 = BinaryTreeNode(7)
node8 = BinaryTreeNode(8)
node9 = BinaryTreeNode(9)
node10 = BinaryTreeNode(10)
node11 = BinaryTreeNode(11)


node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right= node6
node4.right = node7
node6.left = node8
node7.left = node9
node8.right = node11
node9.left = node10


topView(node1)




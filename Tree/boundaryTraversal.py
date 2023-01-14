class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def leftBoundary(root, ans):
    if root is None or (root.left is None and root.right is None):
        return ans

    ans.append(root.data)
    if root.left is not None:
        leftBoundary(root.left, ans)
    else:
        leftBoundary(root.right, ans)


def rightBoundary(root, ans):
    if root is None or (root.left is None and root.right is None):
        return ans

    if root.right is not None:
        rightBoundary(root.right, ans)

    else:
        rightBoundary(root.left, ans)
    ans.append(root.data)


def leafBoundary(root, ans):
    if root is None:
        return ans

    if root.left is None and root.right is None:
        ans.append(root.data)
        return

    leafBoundary(root.left, ans)
    leafBoundary(root.right, ans)

def BoundryTraversal(root):
    ans = []
    if root is None:
        return ans

    ans.append(root.data)
    leftBoundary(root.left, ans)
    leafBoundary(root.left, ans)
    leafBoundary(root.right, ans)
    rightBoundary(root.right, ans)

    return ans


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
node3.right = node7
node3.left = node8

print(BoundryTraversal(node1))

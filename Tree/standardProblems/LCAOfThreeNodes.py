'''You have been given a Binary Tree of 'N' nodes where the nodes have integer values and three integers 'N1', 'N2', and 'N3'. Find the LCA(Lowest Common Ancestor) of the three nodes represented by the given three('N1', 'N2', 'N3') integer values in the Binary Tree.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lcaOfThreeNodesHelper(root, nodepath, node):
    if root is None:
        return False

    nodepath.append(root.data)
    
    if root.data == node:
        return True

    leftsubtree = lcaOfThreeNodesHelper(root.left, nodepath, node)
    rightsubtree = lcaOfThreeNodesHelper(root.right, nodepath, node)

    if leftsubtree or rightsubtree:
        return True

    del nodepath[-1]

    return False


def lcaOfThreeNodes(root, node1, node2, node3):
    '''Time Complexity
O(N), where N is the total number of nodes in the given binary tree.

 

In the worst case, the tree is traversed thrice to find paths of N1, N2, and N3 O(N), and then the stored path list O(N) is traversed. Thus a total of O(N).

Space Complexity
O(N), where N is the total number of nodes in the given binary tree.

 

In the worst case, we will store all the nodes in the list as a path from the root to the node. And we will have all the nodes of the Binary Tree in the recursion stack O(N). Thus a total of O(N).'''

    node1path = []
    node2path = []
    node3path = []

    lcaOfThreeNodesHelper(root, node1path, node1)
    lcaOfThreeNodesHelper(root, node2path, node2)
    lcaOfThreeNodesHelper(root, node3path, node3)

    print(node1path)
    print(node2path)
    print(node3path)
    i = 0

    while i<len(node1path) and i<len(node2path) and i<len(node3path):
        if node1path[i] != node2path[i] or node2path[i] != node3path[i] or node3path[i] != node1path[i]:
            break
        i+=1

    return node1path[i-1]


def lcaOfThreeNode2(root, node1, node2, node3):
    ''' Time Complexity
    O(N),  where N is the number of nodes in the Binary Tree.
    In the worst case, we will perform a full Depth-First-Search of the Binary Tree.    Hence, complexity is linear.
    Space Complexity
    O(N), where N is the number of nodes in the Binary Tree.

    In the worst case, we will have all the nodes of the Binary Tree in the recursion   stack. Hence, complexity is linear.'''
    if root == None:
        return None

    if root.data == node1 or root.data == node2 or root.data == node3:
        return root

    left = lcaOfThreeNode2(root.left, node1, node2, node3)
    right = lcaOfThreeNode2(root.right, node1, node2, node3)

    if left != None and right != None:
        return root

    elif left != None:
        return left 

    else:
        return right
    


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node1.left = node2
node1.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.left = node9
node6.right = node10

k1,k2,k3 = input().split()
k1 = int(k1)
k2 = int(k2)
k3 = int(k3)
print(lcaOfThreeNodes(node1, k1, k2, k3))
print(lcaOfThreeNode2(node1, k1, k2, k3).data)


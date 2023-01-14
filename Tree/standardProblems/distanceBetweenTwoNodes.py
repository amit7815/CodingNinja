''' Given a binary tree and the value of two nodes, find the distance between the given two nodes of the Binary Tree.
Distance between two nodes is defined as the minimum number of edges in the path from one node to another.'''

def findLca(root, node1, node2):
    if root == None:
        return None

    if root.data == node1 or root.data == node2:
        return root

    left = findLca(root.left, node1, node2)
    right = findLca(root.right, node1, node2)

    if left != None and right != None:
        return root

    elif left != None:
        return left

    else:
        return root


def findLevel(root, node, level):
    if root == None:
        return -1

    if root.data == node:
        return level

    left = findLevel(root.left, node, level+1)

    if left == -1:
        left = findLevel(root.right, node, level+1)

    else:
        return left



def distanceBetweenTwoNodes(root, node1, node2):
    '''Time Complexity
    O(N), where ‘N’ is the number of nodes in the given binary tree.

    Since in the worst case (Skewed Trees), we might be visiting all the nodes of the   binary tree.

    Time complexities of the functions we have used.Therefore, the overall time     complexity will be linear, i.e. O(N).

    Space Complexity
    O(N), Where ‘N’ is the number of nodes in the given binary tree.

    We are using O(H) extra space for the call stack where ‘H’ is the height of the     tree, and height of a skewed binary tree could be ‘N’ in the worst case.'''
    lca = findLca(root, node1, node)

    if lca == None:
        return -1

    d1 = findLevel(lca, node1, 0)
    d2 = findLevel(lca, node2, 0)

    if d1 == -1 or d2 == -1:
        return -1

    return d1+d2
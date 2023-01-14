''' You are given a binary tree . You are supposed to return the length of the 
diameter of the tree
The diameter of a binary tree is the  length  of the longest path between any two 
end nodes in a tree'''

class Node:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

def diameterHelper(root):
    if root is None:
        return 0, -1
    option2 ,lh = diameterHelper(root.left)
    option3 , rh = diameterHelper(root.right)
    h = 1 + max(lh,rh)
    option1 = lh+rh
    return max(option1 + 2, option2, option3), h

def diameter(root):
    ans = diameterHelper(root)
    return ans[0], ans[1]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node7 = Node(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node7

print(diameter(node1))
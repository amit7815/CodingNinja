''' print successor(baad wala) of the given node while inorder traversal'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorderTraversalHelper(root, ans):
    if root is None:
        return ans

    inorderTraversalHelper(root.left, ans)
    ans.append(root.data)
    inorderTraversalHelper(root.right, ans)

def inorderTraversal(root, node):
    '''T --> O(N), S--> O(N)'''
    ans = []
    inorderTraversalHelper(root, ans)
    for i in range(len(ans)):
        if i != len(ans)-1:
            if ans[i] == node:
                return ans[i+1]
        else:
            return None


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


data = int(input())
print(inorderTraversal(node1,data))


            


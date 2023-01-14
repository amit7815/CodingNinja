'''  You have given a binary tree of integers . You are supposed to return the reverse 
of level order travrsal'''

import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def reverseTraversal(root):
    if root is None:
        return None

    q = queue.Queue()
    q.put(root)
    ans = []
    while not q.empty():
        qSize = q.qsize()
        while qSize != 0:
            current_node = q.get()
            ans.append(current_node.data)
            if current_node.left is not None:
                q.put(current_node.left)
            if current_node.right is not None:
                q.put(current_node.right)
            qSize -= 1

    return ans[::-1]


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
node3.right = node7

print(reverseTraversal(node1))
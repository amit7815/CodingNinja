import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def spiralOrder(root):
    spiral = []
    if root is None:
        return []

    leftToright = []
    rightToleft = []

    leftToright.append(root)

    while len(leftToright):
        while len(leftToright):
            element = leftToright.pop()
            data = element.data
            spiral.append(data)

            if element.left is not None:
                rightToleft.append(element.left)
            if element.right is not None:
                rightToleft.append(element.right)
        

        while len(rightToleft):
            element = rightToleft.pop()
            data = element.data
            spiral.append(data)

            if element.right is not None:
                leftToright.append(element.right)
            if element.left is not None:
                leftToright.append(element.left)

    return spiral


        

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
node11 = Node(11)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node8
node3.right = node7
node3.left = node6
node4.right = node9
node5.left = node10
node5.right = node11

print(spiralOrder(node1))
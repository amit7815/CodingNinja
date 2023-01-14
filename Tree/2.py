
class BinaryTreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def spiralOrder(root):
    ans = []
    if root is None :
        return ans
    q = Queue()
    q.put(root)
    level = 0
    while not q.empty() :
        qSize = q.qsize()
        while qSize != 0 :
        	current_node = q.get()
        	ans.append(current_node.data)                                                                                                                                                                                                                                                                                                                                                                                                                                     
            if level % 2 == 0 :
                if current_node.right is not None:
                    q.put(current_node.right)
                if current_node.left is not None:
                    q.put(current_node.left)
                qSize -= 1
            else:
                if current_node.left is not None:
                    q.put(current_node.left)
                if current_node.right is not None:
                    q.put(current_node.right) 
                qSize -= 1
        level += 1
    return ans



node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)
node7 = BinaryTreeNode(7)
node8 = BinaryTreeNode(8)

node1.left = node2
node1.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.right = node7
node4.left = node8

print(spiralOrder(node1))

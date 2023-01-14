''' You are given an array storing values of n nodes of a binary tree . Your task is
to construct a complete binary tree from the given array in level oredre fashion i.e
elements from left in the array will be filled in the tree level-wise starting from 
level 0

A binary tree is complete Binary tree if all the levels are completely filled except 
possibly the last level and the last level has all nodes as left as possible  '''
import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructCBTHelper(arr, root, index):
    # T --> O(N) and S --> O(logN) or O(Height)
    if index < len(arr):
        root = Node(arr[index])
        root.left = constructCBTHelper(arr, root.left, 2*index+1)
        root.right = constructCBTHelper(arr, root.right, 2*index+2)
    return root

    
def constructCBT(arr):
    root = constructCBTHelper(arr, None, 0)
    return root


def printTreeLevelWise(root):
    if root is None:
        return 

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        qSize = q.qsize()

        while qSize:
            current_node = q.get()
            print(current_node.data, end= " ")

            if current_node.left is not None:
                q.put(current_node.left)

            if current_node.right is not None:
                q.put(current_node.right)

            qSize -= 1
            if qSize == 0:
                print()


arr = [int(ele) for ele in input().split()]

root = constructCBT(arr)
printTreeLevelWise(root)
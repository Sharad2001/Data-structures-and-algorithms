import sys

import sys

sys.setrecursionlimit(100000)
from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def LeftBoundary(root, lst):
    Queue = []

    Queue.append(root)
    while (len(Queue)):
        rootn = Queue.pop()
        if (rootn.left is not None):
            lst.append(rootn.left.data)
            Queue.append(rootn.left)
        elif (rootn.right is not None):
            lst.append(rootn.right.data)
            Queue.append(rootn.right)

        else:
            return lst

    return lst

def RightBoundary(root, lst2):
    Queue = []
    Queue.append(root)
    while (len(Queue)):
        rootn = Queue.pop()
        if (rootn.right is not None):
            lst2.append(rootn.right.data)
            Queue.append(rootn.right)
        elif (rootn.left is not None):
            lst2.append(rootn.left.data)
            Queue.append(rootn.left)
        else:
            return lst2

    return lst2

def LeafNodes(root, lst1):
    lstack = []
    lstack.append(root)
    while (len(lstack)):
        rootn = lstack.pop()
        if rootn.left is not None:
            lstack.append(rootn.left)
        if rootn.right is not None:
            lstack.append(rootn.right)
        if rootn.left == None and rootn.right == None:
            lst1.append(rootn.data)
    return lst1

class Solution:
    def printBoundaryView(self, root):

        lst = []
        lst.append(root.data)
        if (root.left is not None):
            LeftBoundary(root, lst)
            lst.pop()

        if (root.left is not None):
            lst1 = []
            LeafNodes(root, lst1)

            lst1.reverse()
            if root.right is not None:
                lst1.pop()

            for i in lst1:
                lst.append(i)
        if (root.right is not None):
            lst2 = []
            RightBoundary(root, lst2)

            lst2.reverse()

            for i in lst2:
                lst.append(i)

        return lst

def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    s = input()
    root = buildTree(s)
    obj = Solution()
    res = obj.printBoundaryView(root)
    for i in res:
        print(i, end=" ")
    print('')
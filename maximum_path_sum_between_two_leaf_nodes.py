from math import inf
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def recur(nd):
    if nd is None:
        return -inf, -inf
    if nd.left is None and nd.right is None:
        return nd.data, -inf
    Lsidemax, Lfullmax = recur(nd.left)
    Rsidemax, Rfullmax = recur(nd.right)
    sidemax = max(Lsidemax + nd.data, Rsidemax + nd.data)
    fullmax = max(Lfullmax, Rfullmax, Lsidemax + Rsidemax + nd.data)
    return sidemax, fullmax


class Solution:
    def maxPathSum(self, root):
        Lsidemax, Lfullmax = recur(root.left)
        Rsidemax, Rfullmax = recur(root.right)
        if Lsidemax == -inf:
            Lsidemax = 0
        if Rsidemax == -inf:
            Rsidemax = 0
        ans = max(Lfullmax, Rfullmax, Lsidemax + Rsidemax + root.data)
        return ans

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
    ob = Solution()
    print(ob.maxPathSum(root))
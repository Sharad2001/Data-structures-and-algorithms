from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def isBalanced(self, root):

        # add code here
        if root == None:
            return 1
        lh = self.isBalanced(root.left)
        rh = self.isBalanced(root.right)
        if lh == 0 or rh == 0 or abs(lh - rh) > 1:
            return 0
        return 1 + max(rh, lh)


def buildTree(s):
    if (len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))

    root = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
    size = size + 1

    i = 1
    while (size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size = size - 1

        currVal = ip[i]

        if (currVal != "N"):
            currNode.left = Node(int(currVal))

            q.append(currNode.left)
            size = size + 1
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        if (currVal != "N"):
            currNode.right = Node(int(currVal))

            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    s = input()
    root = buildTree(s)
    ob = Solution()
    if ob.isBalanced(root):
        print(1)
    else:
        print(0)
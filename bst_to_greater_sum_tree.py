from collections import deque
class Solution:
    def transformTree(self, root):
        arr = [0]
        self.dfs(root, arr)

    def dfs(self, root, arr):
        if root == None:
            return

        self.dfs(root.right, arr)
        temp = arr[0]
        arr[0] += root.data
        root.data = temp
        self.dfs(root.left, arr)


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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


def inOrder(root):
    if root == None:
        return

    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


if __name__ == "__main__":
    s = input()
    root = buildTree(s)
    ob = Solution()

    ob.transformTree(root)
    inOrder(root)

    print()
def traverse(root, ans, level):
    if root == None:
        return
    if len(ans) < level + 1:
        ans.append([root.data])
    traverse(root.left, ans, level + 1)
    traverse(root.right, ans, level + 1)

def LeftView(root):
    tree = []
    level = 0
    traverse(root, tree, level)
    ans = []
    for branch in tree:
        ans.append(branch[0])
    return ans

from collections import deque

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

if __name__ == "__main__":
    s = input()
    root = buildTree(s)
    result = LeftView(root)
    for value in result:
        print(value, end=" ")
    print()
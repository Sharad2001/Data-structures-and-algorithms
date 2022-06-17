def insert(root, Key):
    if root == None:
        return Node(Key)
    if root.data == Key:
        return root
    elif root.data > Key:
        root.left = insert(root.left, Key)
    else:
        root.right = insert(root.right, Key)
    return root

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

def inOrder(n):
    if n is None:
        return
    inOrder(n.left)
    print(n.data, end=' ')
    inOrder(n.right)

if __name__ == "__main__":
    s = input()
    root = buildTree(s)
    k = int(input())
    insert(root, k)
    inOrder(root)
    print()
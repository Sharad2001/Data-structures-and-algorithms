def findSpiral(root):
    que, out = [], []
    turn = "right"
    que.append(root)
    while bool(que):
        if turn == "right":
            size = len(que)
            for i in range(size):
                node = que.pop()
                if node is not None:
                    out.append(node.data)
                    if node.right is not None:
                        que.insert(0, node.right)
                    if node.left is not None:
                        que.insert(0, node.left)
            turn = "left"
        else:
            size = len(que)
            for i in range(size):
                node = que.pop(0)
                if node is not None:
                    out.append(node.data)
                    if node.left is not None:
                        que.append(node.left)
                    if node.right is not None:
                        que.append(node.right)
            turn = "right"
    return out

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
    result = findSpiral(root)
    for value in result:
        print(value, end=" ")
    print()
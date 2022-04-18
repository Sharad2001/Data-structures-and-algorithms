from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def preorder(root):
    res = []
    queue = []
    size = 0
    queue.append(root)
    size += 1
    while size > 0:
        currentNode = queue[0]
        queue = queue[1:]
        size = size - 1

        if (currentNode.data != None):
            res.append(currentNode.data)

        if (currentNode.right and currentNode.right.data != None):
            queue.insert(0, currentNode.right)
            size = size + 1

        if (currentNode.left and currentNode.left.data != None):
            queue.insert(0, currentNode.left)
            size = size + 1
    return res

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
    res = preorder(root)
    for i in res:
        print(i, end=" ")
    print()
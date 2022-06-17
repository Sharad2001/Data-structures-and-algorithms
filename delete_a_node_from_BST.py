def deleteNode(root, X):
    def get_succ(curr, data):
        while curr.left != None:
            curr = curr.left
        return curr.data

    def delete(curr, val):
        if curr == None:
            return
        if val < curr.data:
            curr.left = delete(curr.left, val)
        if val > curr.data:
            curr.right = delete(curr.right, val)
        if curr.data == val:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                succ = get_succ(curr.right, val)
                curr.data = succ
                curr.right = delete(curr.right, succ)
        return curr

    return delete(root, X)

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

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=' '),
        inorder(root.right)

if __name__ == "__main__":
    s = input()
    x = int(input())
    root = buildTree(s)
    root = deleteNode(root, x)
    inorder(root)
    print()
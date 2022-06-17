def levelOrder(root):
    a = []
    q = []
    q.append(root)
    while q:
        node = q.pop(0)
        a.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return a

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def height(node):
    if node is None:
        return 0
    else :
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1

def insert(root,node):
    if root == None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    root = Node(arr[0])
    for i in range(1, n):
        insert(root, Node(arr[i]))
    res = levelOrder(root)
    for i in range (len (res)):
        print (res[i], end=" ")
    print()
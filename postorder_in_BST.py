def postOrder(root):
    res = []
    if not root:
        return res
    res.extend(postOrder(root.left))
    res.extend(postOrder(root.right))
    res.append(root.val)
    return res

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, node):
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
    res = postOrder(root)
    for i in range(len(res)):
        print(res[i], end=" ")
    print()
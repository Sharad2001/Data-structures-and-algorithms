def buildTree(preorder, inorder, n):
    if not preorder or not inorder:
        return None
    val = preorder[0]
    preorder.pop(0)
    root = Node(val)

    if inorder.index(val) >= 0:
        root.left = buildTree(preorder, inorder[:inorder.index(val)], n)

    if inorder.index(val) < n:
        root.right = buildTree(preorder, inorder[inorder.index(val) + 1:], n)

    return root


def post_order(pre, size):
    # code here
    inorder = pre.copy()
    inorder.sort()
    return buildTree(pre, inorder, size)

class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':
    size = int(input())
    pre = [int(x) for x in input().split()]

    root = post_order(pre, size)

    postOrd(root)
    print()
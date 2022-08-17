class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None
def merge(a, b):
    if (a == None):
        return b
    if (b == None):
        return a
    result = None
    if (a.data < b.data):
        result = a
        result.bottom = merge(a.bottom, b)
    else:
        result = b
        result.bottom = merge(a, b.bottom)
    result.next = None
    return result


def flatten(root):
    if (root == None or root.next == None):
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root


def printList(node):
    while (node is not None):
        print(node.data, end=" ")
        node = node.bottom

    print()

if __name__ == "__main__":
    head = None
    N = int(input())
    arr = []

    arr = [int(x) for x in input().strip().split()]
    temp = None
    tempB = None
    pre = None
    preB = None

    flag = 1
    flag1 = 1
    listo = [int(x) for x in input().strip().split()]
    it = 0
    for i in range(N):
        m = arr[i]
        m -= 1
        a1 = listo[it]
        it += 1
        temp = Node(a1)
        if flag == 1:
            head = temp
            pre = temp
            flag = 0
            flag1 = 1
        else:
            pre.next = temp
            pre = temp
            flag1 = 1

        for j in range(m):
            a = listo[it]
            it += 1
            tempB = Node(a)
            if flag1 == 1:
                temp.bottom = tempB
                preB = tempB
                flag1 = 0
            else:
                preB.bottom = tempB
                preB = tempB
    root = flatten(head)
    printList(root)
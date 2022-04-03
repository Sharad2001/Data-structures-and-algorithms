def isSorted(head):
    curr = head
    inc = 1
    dec = 1
    while curr.next != None:
        if curr.next.data > curr.data:
            dec = 0
        if curr.next.data < curr.data:
            inc = 0
        curr = curr.next
    return inc or dec

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]

    ll = Llist()
    tail = None

    for nodeData in arr:
        tail = ll.insert(nodeData, tail)

    res=isSorted(ll.head)
    print(res)
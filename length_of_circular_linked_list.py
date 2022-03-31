def getLength(head):
    l = []
    temp = head
    if head == None:
        return 0
    while 1:
        l.append(temp.data)
        temp = temp.next
        if temp == head:
            return len(l)

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
    tail.next = ll.head
    print(getLength(ll.head))
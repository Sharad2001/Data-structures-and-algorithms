def insertInSorted(head, data):
    temp = Node(data)
    if head == None:
        return temp
    elif data < head.data:
        temp.next = head
        return temp
    else:
        curr = head
        while curr.next != None and curr.next.data < data:
            curr = curr.next

        temp.next = curr.next
        curr.next = temp
        return head
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

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    data = int(input())
    ll = Llist()
    tail = None

    for nodeData in arr:
        tail = ll.insert(nodeData, tail)

    res = insertInSorted(ll.head, data)
    printList(res)
    print()
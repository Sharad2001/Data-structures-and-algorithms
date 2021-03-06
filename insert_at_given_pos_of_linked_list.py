def insertAtPosition(head,pos,data):

    size = 0
    temp = Node(data)
    while head != None:
        size += 1
        if size == pos:
            temp.next = head.next
            head.next = temp
            return
        head = head.next
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
        print(head.data,end=' ')
        head=head.next

if __name__ == '__main__':

    n = int(input())
    arr = [int(x) for x in input().split()]
    pos,data=[int(x) for x in input().split()]

    ll = Llist()
    tail = None

    for nodeData in arr:
        tail = ll.insert(nodeData, tail)

    insertAtPosition(ll.head,pos,data)
    printList(ll.head)
    print()
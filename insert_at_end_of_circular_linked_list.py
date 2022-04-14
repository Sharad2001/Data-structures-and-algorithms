def insertInTail(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.data, temp.data = temp.data, head.data
        return temp

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

def displayList(head):
    t=head
    while t.next!=head:
        print(t.data,end=' ')
        t=t.next
    print(t.data,end=' ')

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    data=int(input())

    ll = Llist()
    tail = None

    for nodeData in arr:
        tail = ll.insert(nodeData, tail)
    tail.next=ll.head

    resHead=insertInTail(ll.head,data)
    displayList(resHead)
    print()
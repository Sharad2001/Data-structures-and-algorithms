class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtPosition(head,pos,data):
    #code here
    temp = Node(data)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    for i in range(pos-1):
        curr = curr.next
        if curr == head:
            return head
    temp.next = curr.next
    curr.next = temp
    return head

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
    pos,data=[int(x) for x in input().split()]

    ll = Llist()
    tail = None

    for nodeData in arr:
        tail = ll.insert(nodeData, tail)
    #making circular
    tail.next=ll.head

    insertAtPosition(ll.head,pos,data)
    displayList(ll.head)
    print()
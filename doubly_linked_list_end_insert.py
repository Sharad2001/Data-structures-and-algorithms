class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def insertInTail(head,data):

    temp = Node(data)
    if head == None:
        return temp
    else:
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = temp
        temp.prev = curr
        return head

class doublyLL:
    def __init__(self):
        self.head=None

    def insert(self,tail,data):
        head=self.head

        node=Node(data)

        if not head:

            self.head=node
            return node

        tail.next=node
        node.prev=tail
        return node

def displayList(head):
    while head:
        print(head.data,end=' ')
        pvs=head
        head=head.next
    print()

    while pvs:
        print(pvs.data,end=' ')
        pvs=pvs.prev

if __name__=='__main__':
    n=int(input())
    arr=[int(x) for x in input().split()]
    tailData=int(input())

    dll=doublyLL()

    tail=None

    for nodeData in arr:
        tail=dll.insert(tail,nodeData)

    dll.head=insertInTail(dll.head,tailData)
    displayList(dll.head)
    print()
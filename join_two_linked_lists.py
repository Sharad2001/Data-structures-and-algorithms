def joinTheLists(head1, head2):
    if head1 == None:
        return head2
    curr1 = head1
    while curr1.next != None:
        curr1 = curr1.next
    curr1.next = head2
    return head1

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
    tmp = head
    while (head != None):
        print(head.data, end=" ")
        head = head.next
    head = tmp
    print()

if __name__ == '__main__':
    n = int(input("Enter the number of elements of first linked list: "))
    arr = [int(x) for x in input("Enter the elements: ").split()]
    m = int(input("Enter the number of elements of second linked list: "))
    brr = [int(x) for x in input("Enter the element of second linked list: ").split()]
    ll1 = Llist()
    ll2 = Llist()
    tail1 = None
    tail2 = None
    for nodeData in arr:
        tail1 = ll1.insert(nodeData, tail1)

    for nodeData in brr:
        tail2 = ll2.insert(nodeData, tail2)

    res = joinTheLists(ll1.head, ll2.head)
    printList(res)
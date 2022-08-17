class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
def sortedMerge(head1, head2):
    dummyNode = Node(0)
    tail = dummyNode
    while True:
        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    return dummyNode.next



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    n, m = map(int, input().strip().split())

    a = LinkedList()  # create a new linked list 'a'.
    b = LinkedList()  # create a new linked list 'b'.

    nodes_a = list(map(int, input().strip().split()))
    nodes_b = list(map(int, input().strip().split()))

    for x in nodes_a:
        a.append(x)

    for x in nodes_b:
        b.append(x)

    printList(sortedMerge(a.head, b.head))
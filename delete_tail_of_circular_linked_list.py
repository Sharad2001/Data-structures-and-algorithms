class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteTail(head):
    # code here
    if head == None:
        return None
    if head.next == head:
        return None
    curr = head
    while True:
        if curr.next.next == head:
            break
        curr = curr.next
    curr.next = head
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
    t = head
    while t.next != head:
        print(t.data, end=' ')
        t = t.next
    print(t.data, end=' ')


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        tail.next = ll.head

        deleteTail(ll.head)
        displayList(ll.head)
        print()
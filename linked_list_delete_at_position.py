def deleteAtPosition(head, pos):
    if head == None:
        return
    if pos == 1:
        return head.next
    index = 1
    curr = head
    prev = head
    temp = head
    while curr != None:
        if index == pos:
            temp = curr.next
            break
        prev = curr
        curr = curr.next
        index += 1
    prev.next = temp
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
    tmp = head
    while tmp != None:
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    x = int(input())

    ll = Llist()
    tail = None

    for nodeData in arr:
        tail = ll.insert(nodeData, tail)

    res = deleteAtPosition(ll.head, x)
    printList(res)
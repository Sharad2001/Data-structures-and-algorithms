def searchLinkedList(head,x):
    #code here
    res = []
    curr = head
    while curr != None:
        res.append(curr.data)
        curr = curr.next
    if x in res:
        return 1
    else:
        return 0
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
    arr = [int(x) for x in input("Enter the elements: ").split()]
    x=int(input("Enter the element which want to search: "))

    ll = Llist()
    tail = None

    for nodeData in arr:
        tail = ll.insert(nodeData, tail)

    res=searchLinkedList(ll.head,x)
    print(res)
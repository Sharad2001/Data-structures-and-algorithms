def areIdentical(head1, head2):
    curr1 = head1
    curr2 = head2
    while curr1:
        if curr1.data != curr2.data:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    else:
        return True

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    head1 = createList(arr, n)
    n = int(input())
    arr = list(map(int, input().strip().split()))
    head2 = createList(arr, n)
    if (areIdentical(head1, head2)):
        print('Identical')
    else:
        print('Not identical')
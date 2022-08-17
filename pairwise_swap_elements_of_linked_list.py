class Solution:
    def pairWiseSwap(self, head):
        if not (head and head.next):
            return head
        head.next.next, head.next, head = head, self.pairWiseSwap(head=head.next.next), head.next
        return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]

    lis = LinkedList()
    for i in arr:
        lis.insert(i)

    dict1 = {}
    temp = lis.head
    while temp:
        dict1[temp] = temp.data
        temp = temp.next

    failure = LinkedList()
    failure.insert(-1)

    head = Solution().pairWiseSwap(lis.head)

    temp = head
    f = 0
    while temp:
        if dict1[temp] != temp.data:
            f = 1;
        temp = temp.next

    if f:
        printList(failure)
    else:
        printList(head)
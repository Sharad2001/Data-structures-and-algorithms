class Solution:
    def rotate(self, head, k):
        if k == 0:
            return
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = head
        curr = head
        for i in range(k - 1):
            curr = curr.next
        head = curr.next
        curr.next = None
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
    k = int(input())

    lis = LinkedList()
    for i in arr:
        lis.insert(i)

    head = Solution().rotate(lis.head, k)
    printList(head)
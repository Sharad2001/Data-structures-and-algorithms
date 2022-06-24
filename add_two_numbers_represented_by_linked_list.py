class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

    def addTwoLists(self, first, second):
        rev_l1 = self.reverse(first)
        rev_l2 = self.reverse(second)
        l1 = rev_l1
        l2 = rev_l2
        dummy = Node(None)
        temp = dummy
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.data
                l1 = l1.next
            if l2:
                sum += l2.data
                l2 = l2.next
            sum += carry
            carry = sum // 10
            node = Node(sum % 10)
            temp.next = node
            temp = temp.next
        ans = self.reverse(dummy.next)
        return ans

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

if __name__ == '__main__':
    n = int(input())
    arr1 = (int(x) for x in input().split())
    LL1 = LinkedList()
    for i in arr1:
        LL1.insert(i)

    m = int(input())
    arr2 = (int(x) for x in input().split())
    LL2 = LinkedList()
    for i in arr2:
        LL2.insert(i)

    res = Solution().addTwoLists(LL1.head, LL2.head)
    printList(res)
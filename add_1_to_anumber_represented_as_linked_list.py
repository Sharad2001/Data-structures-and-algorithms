class Solution:
    def reverse(self, head):
        if not head:
            return
        curNode = head
        prevNode = head
        nextNode = head.next
        curNode.next = None
        while nextNode:
            curNode = nextNode
            nextNode = nextNode.next
            curNode.next = prevNode
            prevNode = curNode
        return curNode

    def addOne(self, head):
        head = self.reverse(head)
        k = head
        carry = 0
        prev = None
        head.data += 1
        while (head != None) and (head.data > 9 or carry > 0):
            prev = head
            head.data += carry
            carry = head.data // 10
            head.data = head.data % 10
            head = head.next
        if carry > 0:
            prev.next = Node(carry)
        return self.reverse(k)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next

if __name__ == '__main__':
    num = input()
    ll = LinkedList()
    for digit in num:
        ll.insert(int(digit))

    resHead = Solution().addOne(ll.head)
    PrintList(resHead)
    print()
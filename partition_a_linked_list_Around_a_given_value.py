class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def partition(self, head, x):
        #code here
        a = Node(-1)
        b = Node(-1)
        c = Node(-1)
        ans1 = a
        ans2 = b
        ans3 = c
        while head:
            if head.data < x:
                a.next = Node(head.data)
                a = a.next
            elif head.data > x:
                c.next = Node(head.data)
                c = c.next
            else:
                b.next = Node(head.data)
                b = b.next
            head = head.next
        b.next = ans3.next
        a.next = ans2.next
        return ans1.next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")

            temp = temp.next
        print()

if __name__ == '__main__':
    llist = LinkedList()
    n = input()
    values = list(map(int, input().split()))
    for i in reversed(values):
        llist.push(i)
    k = int(input())
    new_head = LinkedList()
    ob=Solution()
    new_head = ob.partition(llist.head, k)
    llist.head = new_head
    llist.printList()
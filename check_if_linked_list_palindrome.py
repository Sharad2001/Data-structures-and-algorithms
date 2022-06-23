class Solution:
    def isPalindrome(self, head):
        stack = []
        curr = head
        ispalin = True
        while curr != None:
            stack.append(curr.data)
            curr = curr.next

        while head != None:
            i = stack.pop()
            if head.data == i:
                ispalin = True
            else:
                ispalin = False
                break
            head = head.next
        return ispalin

import atexit
import io
import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

if __name__ == '__main__':
    n = int(input())
    a = LinkedList()
    nodes_a = list(map(int, input().strip().split()))
    for x in nodes_a:
        a.append(x)

    if Solution().isPalindrome(a.head):
        print(1)
    else:
        print(0)
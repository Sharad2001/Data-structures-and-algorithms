def sumOfElements(head):
    # code here
    sum = 0
    curr = head
    while curr != None:
        sum = sum + curr.data
        curr = curr.next
    return sum

import io
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # append at the end of the list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next


if __name__ == '__main__':
    n = int(input())
    a = LinkedList()
    nodes = list(map(int, input().strip().split()))  # list containing nodes
    for x in nodes:
        node = Node(x)  # create a new node
        a.append(node)
    print(sumOfElements(a.head))

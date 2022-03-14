class Solution:

    # Function to count nodes of a linked list.
    def getCount(self, head_node):
        res = []
        curr = head_node
        while curr != None:
            res.append(curr.data)
            curr = curr.next
        return len(res)

import io
import sys


# Node class
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
    a = LinkedList()
    nodes = list(map(int, input("Enter the elements of linked list: ").strip().split()))  # list containing nodes
    for x in nodes:
        node = Node(x)  # create a new node
        a.append(node)
    print(Solution().getCount(a.head))

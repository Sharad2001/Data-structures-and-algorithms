def maximum(head):
    # code here
    res1 = []
    curr = head
    while curr != None:
        res1.append(curr.data)
        curr = curr.next
    return max(res1)


def minimum(head):
    # code here
    res2 = []
    curr = head
    while curr != None:
        res2.append(curr.data)
        curr = curr.next
    return min(res2)

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
    print(maximum(a.head), end=" ")
    print(minimum(a.head))
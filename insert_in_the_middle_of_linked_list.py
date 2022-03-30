def insertInMid(head, node):
    # code here
    head_counter = head
    counter = 1
    while (head_counter.next != None):
        counter += 1
        head_counter = head_counter.next

    mid = counter // 2
    if (counter % 2 == 0):
        mid = mid - 1
    node_counter = head
    for i in range(mid):
        node_counter = node_counter.next

    node.next = node_counter.next
    node_counter.next = node

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

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
        return

    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


if __name__ == '__main__':
    n = int(input())
    a = LinkedList()
    nodes = list(map(int, input().strip().split()))
    for x in nodes:
        a.append(x)
    mid_elem = int(input())
    insertInMid(a.head, Node(mid_elem))
    a.printList()
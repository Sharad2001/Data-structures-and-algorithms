def getNthFromLast(head, n):
    temp = head
    length = 0
    while temp is not None:
        temp = temp.next
        length += 1

    if n > length:
        return -1
    temp = head
    for i in range(0, length - n):
        temp = temp.next
    return temp.data

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
    def __init__(self, data):  # data -> value stored in node
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
    n, nth_node = map(int, input().strip().split())
    a = LinkedList()  # create a new linked list 'a'.
    nodes_a = list(map(int, input().strip().split()))
    for x in nodes_a:
        a.append(x)  # add to the end of the list
    print(getNthFromLast(a.head, nth_node))
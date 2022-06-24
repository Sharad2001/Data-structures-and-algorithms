class Solution:
    def deleteNode(self, curr_node):
        temp = curr_node.next
        curr_node.data = temp.data
        curr_node.next = temp.next

import atexit
import io
import sys

sys.setrecursionlimit(5000)
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

    def getNode(self, value):
        curr_node = self.head
        while (curr_node.next and curr_node.data != value):
            curr_node = curr_node.next
        if (curr_node.data == value):
            return curr_node
        else:
            return None

    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

if __name__ == '__main__':
    n = int(input())
    a = LinkedList()
    nodes = list(map(int, input().strip().split()))
    for x in nodes:
        a.append(x)
    del_elem = int(input())
    to_delete = a.getNode(del_elem)
    Solution().deleteNode(to_delete)
    a.printList()
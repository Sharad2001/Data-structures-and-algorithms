def intersetPoint(head1, head2):
    c1 = getCount(head1)
    c2 = getCount(head2)
    if c1 > c2:
        d = c1 - c2
        return _intersetPoint(d, head1, head2)
    else:
        d = c2 - c1
        return _intersetPoint(d, head2, head1)

def _intersetPoint(d, head1, head2):
    curr1 = head1
    curr2 = head2
    for i in range(d):
        if curr1 is None:
            return -1
        curr1 = curr1.next
    while curr1 != None and curr2 != None:
        if curr1 is curr2:
            return curr1.data
        curr1 = curr1.next
        curr2 = curr2.next
    return -1

def getCount(head):
    curr = head
    count = 0
    while curr != None:
        count += 1
        curr = curr.next
    return count

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
        temp = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next

if __name__ == '__main__':
    x, y, z = map(int, input().strip().split())
    a = LinkedList()
    b = LinkedList()
    nodes_a = list(map(int, input().strip().split()))
    nodes_b = list(map(int, input().strip().split()))
    nodes_common = list(map(int, input().strip().split()))

    for x in nodes_a:
        node = Node(x)
        a.append(node)
    for x in nodes_b:
        node = Node(x)
        b.append(node)

    for i in range(len(nodes_common)):
        node = Node(nodes_common[i])
        a.append(node)
        if i == 0:
            b.append(node)
    print(intersetPoint(a.head, b.head))
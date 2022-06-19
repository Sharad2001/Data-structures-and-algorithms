class Solution:
    def reverseBetween(self, head, m, n):

        def find_len(head):
            temp = head
            count = 0
            while temp:
                count += 1
                temp = temp.next
            return count

        if not head:
            return
        list_len = find_len(head)

        if m > 1:
            cur_ind = 1
            top = head
            while top and cur_ind < m - 1:
                top = top.next
                cur_ind += 1
        if n < list_len:
            cur_ind = 1
            end = head
            while end and cur_ind < n + 1:
                end = end.next
                cur_ind += 1
        cur_ind = 1
        ptr = head
        while ptr and cur_ind != m:
            ptr = ptr.next
            cur_ind += 1
        count = m
        pre = post = None
        cur = ptr
        while count <= n and cur is not None:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
            count += 1
        new_head = pre

        if m > 1:
            top.next = new_head
            new_head = head
        if n < list_len:
            ptr.next = end
        return new_head

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

    def printList(self, head):
        if head is None:
            print(' ')
            return
        curr_node = head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

if __name__ == '__main__':
    inp = list(map(int, input().split()))
    N = inp[0]
    m = inp[1]
    n = inp[2]

    a = LinkedList()  # create a new linked list 'a'.
    nodes = list(map(int, input().strip().split()))
    for x in nodes:
        a.append(x)
    ob = Solution()
    newhead = ob.reverseBetween(a.head, m, n)
    a.printList(newhead)
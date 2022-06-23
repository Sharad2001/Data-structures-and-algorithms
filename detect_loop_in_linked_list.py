class Solution:
    def detectLoop(self, head):
        slow_p = head
        fast_p = head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    def loopHere(self, pos):
        if pos == 0:
            return
        walk = self.head
        for i in range(1, pos):
            walk = walk.next
        self.tail.next = walk

if __name__ == '__main__':
    n = int(input())
    LL = LinkedList()
    for i in input().split():
        LL.insert(int(i))
    LL.loopHere(int(input()))
    print(Solution().detectLoop(LL.head))
class Solution:
    def sortedListToBST(self, head):
        if head == None:
            return head
        if head.next == None:
            temp = TNode(head.data)
            return temp
        prev, mid = self.middle(head)
        prev.next = None
        nxt = mid.next
        mid.next = None
        root = TNode(mid.data)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(nxt)
        return root

    def middle(self, head):
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev, slow

class LNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class TNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, new_value):
        new_node = LNode(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

def preOrder(root):
    if root == None:
        return

    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

if __name__ == '__main__':
    n = int(input())
    a = LinkedList()
    nodes_a = list(map(int, input().strip().split()))
    for x in nodes_a:
        a.append(x)

    ob = Solution()
    root = ob.sortedListToBST(a.head)
    preOrder(root)
    print()
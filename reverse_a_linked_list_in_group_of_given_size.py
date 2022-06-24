class Solution:
    def reverse(self, head, k):
        if not head or k == 1:
            return head
        dummy = Node(-1)
        dummy.next = head
        prev = dummy
        curr = dummy
        next = dummy
        count = 0
        toloop = 0
        i = 0
        while curr:
            curr = curr.next
            count += 1

        while next:
            curr = prev.next
            next = curr.next
            toloop = count > k and k or count - 1
            for i in range(1, toloop):
                curr.next = next.next
                next.next = prev.next
                prev.next = next
                next = curr.next

            prev = curr
            count -= k
        return dummy.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == '__main__':
    llist = LinkedList()
    n = input()
    values = list(map(int, input().split()))
    for i in reversed(values):
        llist.push(i)
    k = int(input())
    new_head = LinkedList()
    ob = Solution()
    new_head = ob.reverse(llist.head, k)
    llist.head = new_head
    llist.printList()
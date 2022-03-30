class Solution:
    def insertAtBegining(self, head, x):
        newNode = Node(x)
        if not head:
            newNode.next = None
        else:
            newNode.next = head
        head = newNode
        return head

    def insertAtEnd(self, head, x):

        newNode = Node(x)
        if not head:
            newNode.next = None
            head = newNode
        else:
            tmp = head
            while tmp.next:
                tmp = tmp.next
            tmp.next = newNode
        return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


if __name__ == '__main__':
    n = int(input())
    a = LinkedList()

    nodes_info = list(map(int, input().split()))
    for i in range(0, len(nodes_info) - 1, 2):
        if (nodes_info[i + 1] == 0):
            a.head = Solution().insertAtBegining(a.head, nodes_info[i])
        else:
            a.head = Solution().insertAtEnd(a.head, nodes_info[i])
    printList(a.head)

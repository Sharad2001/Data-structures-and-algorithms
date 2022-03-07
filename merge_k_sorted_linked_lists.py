class Solution:
    def mergeKLists(self, arr, K):
        l = []
        for i in arr:
            temp = i
            while temp:
                l.append(temp.data)
                temp = temp.next
        l.sort()
        head = Node(l[0])
        str = head
        for i in range(1, len(l)):
            node = Node(l[i])
            str.next = node
            str = node
        return head
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk = walk.next
    print()

if __name__ == "__main__":

    n = int(input())
    line = [int(x) for x in input().strip().split()]

    heads = []
    index = 0

    for i in range(n):
        size = line[index]
        index += 1

        newList = LinkedList()

        for _ in range(size):
            newList.add(line[index])
            index += 1

        heads.append(newList.head)

    merged_list = Solution().mergeKLists(heads, n)
    printList(merged_list)
class Solution:
    def findMid(self, head):
        if head == None:
            return -1
        count = 0
        curr = head
        while head:
            if (count & 1):
                curr = curr.next
            head = head.next
            count += 1
        return curr.data

class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

if __name__ == '__main__':
    list1 = Linked_List()
    n = int(input())
    values = list(map(int, input().strip().split()))
    for i in values:
        list1.insert(i)
    ob = Solution()
    print(ob.findMid(list1.head))
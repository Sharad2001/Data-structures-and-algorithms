class Solution:
    def segregate(self, head):
        ne = head
        curr = head
        zero = 0
        one = 0
        two = 0

        while curr != None:
            if curr.data == 0:
                zero += 1
            if curr.data == 1:
                one += 1
            if curr.data == 2:
                two += 1
            curr = curr.next
        while zero:
            zero -= 1
            ne.data = 0
            ne = ne.next
        while one:
            one -= 1
            ne.data = 1
            ne = ne.next
        while two:
            two -= 1
            ne.data = 2
            ne = ne.next
        return head


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print()


if __name__ == '__main__':
    n = int(input())
    a = LinkedList()
    nodes_a = list(map(int, input().strip().split()))
    for x in nodes_a:
        a.append(x)
    printList(Solution().segregate(a.head))
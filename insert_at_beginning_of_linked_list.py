class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def insertBegin(head, key):
    temp = Node(key)
    temp.next = head
    return temp

def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next

head = None
head = insertBegin(head, 10)
head = insertBegin(head, 20)
head = insertBegin(head, 30)
head = insertBegin(head, 5)
printList(head)
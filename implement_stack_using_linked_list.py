class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None

    def push(self, data):

        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def pop(self):

        if self.head == None:
            return -1
        ans = self.head.data
        self.head = self.head.next
        return ans

if __name__ == '__main__':
    s = MyStack()
    q = int(input())
    q1 = list(map(int, input().split()))
    i = 0
    while (i < len(q1)):
        if (q1[i] == 1):
            s.push(q1[i + 1])
            i = i + 2
        elif (q1[i] == 2):
            print(s.pop(), end=" ")
            i = i + 1
        elif (s.isEmpty()):
            print(-1)
    print()
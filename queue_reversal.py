def rev(q):
    stack = []
    while not q.empty():
        stack.append(q.queue[0])
        q.get()
    while len(stack) != 0:
        q.put(stack[-1])
        stack.pop()
    return q

from queue import Queue
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    q=Queue(maxsize=n+1)
    for j in a:
        q.put(j)
    q=rev(q)
    for i in range(0,n):
        print(q.get(),end=" ")
    print()
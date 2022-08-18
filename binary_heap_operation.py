def left(pos):
    return (2*pos + 1)


def right(pos):
    return (2*pos + 2)


def parent(pos):
    return (pos-1)//2


def swap(pos1, pos2):
    global heap
    heap[pos1], heap[pos2] = heap[pos2], heap[pos1]


def isLeaf(pos):
    if left(pos) > (curr_size-1):
        return True
    return False


def heapifyT2B(pos):
    if not isLeaf(pos):
        smallest = pos
        if heap[smallest] > heap[left(pos)]:
            smallest = left(pos)
        if heap[smallest] > heap[right(pos)]:
            smallest = right(pos)
        if smallest != pos:
            swap(smallest, pos)
            heapifyT2B(smallest)


def heapifyB2T(pos):
    if pos > 0:
        if heap[pos] < heap[parent(pos)]:
            swap(pos, parent(pos))
            heapifyB2T(parent(pos))


def decreaseKey(pos, val):
    global heap
    if val > heap[pos]:
        return False
    heap[pos] = val
    heapifyB2T(pos)
    return True


def insertKey (x):
    global curr_size, heap
    if curr_size > 100:
        return False
    heap[curr_size] = x
    curr_size += 1
    heapifyB2T(curr_size-1)

#Function to delete a key at ith index.
def deleteKey (i):
    global curr_size
    if i >= curr_size:
        return -1
    decreaseKey(i, -9223372036854775806)
    extractMin()

#Function to extract minimum value in heap and then to store
#next minimum value at first index.
def extractMin ():
    global heap, curr_size
    if curr_size == 0:
        return -1
    top_ele = heap[0]
    heap[0] = heap[curr_size-1]
    curr_size -= 1
    heapifyT2B(0)
    return top_ele


heap = []
curr_size = 0

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    # initialize every globals
    curr_size = 0
    heap = [0 for i in range(n)]
    i = 0
    while i < len(a):
        if a[i] == 1:
            insertKey(a[i + 1])
            i += 1
        elif a[i] == 2:
            deleteKey(a[i + 1])
            i += 1
        else:
            print(extractMin (), end=" ")
        i += 1
    print()
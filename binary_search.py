def bSearch(l, x):
    low = 0
    high = len(l) - 1
    while low < high:
        mid = (low + high) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

l = [int(i) for i in input("Enter the elements of array: ").strip().split()]
x = int(input("Enter the number of which index want to know: "))
print(f"The index will be: {bSearch(l, x)}")
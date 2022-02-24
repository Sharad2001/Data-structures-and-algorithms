def lastOcc(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low+high)//2
        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
        else:
            if mid == len(l) - 1 or l[mid] != l[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1
if __name__ == '__main__':

    l = [int(i) for i in input("Enter the element of the array: ").strip().split()]
    x = int(input("Enter the element which last index want to know: "))
    print(f"Last index of {x} is {lastOcc(l, x)}")
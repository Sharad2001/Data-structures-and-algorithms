def firstInde(l, x):
    low = 0
    high = len(l) - 1
    while low < high:
        mid = (low+high)//2
        if l[mid] > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or l[mid-1] != l[mid]:
                return mid
            else:
                high = mid - 1
    return -1
if __name__ == '__main__':

    l = [int(i) for i in input("Enter the element of array: ").strip().split()]
    x = int(input("Enter the number which first occurence you want to know: "))
    print(f"First occurence of {x} will be at index {firstInde(l, x)}")
class Solution:
    def sort012(self,arr,n):
        x0 = 0
        x1 = 0
        x2 = 0
        for i in range(0, n):
            if arr[i] == 0:
                x0 += 1
            elif arr[i] == 1:
                x1 += 1
            else:
                x2 += 1
        arr.clear()
        for i in range(x0):
            arr.append(0)
        for i in range(x1):
            arr.append(1)
        for i in range(x2):
            arr.append(2)
        return arr

if __name__ == '__main__':
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    ob=Solution()
    ob.sort012(arr,n)
    for i in arr:
        print(i, end=' ')
    print()

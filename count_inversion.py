class Solution:
    def inversionCount(self, arr, n):
        if n == 1:
            return 0
        l = 0
        r = n - 1
        return (self.mergeSort(arr, l, r))

    def mergeSort(self, arr, l, r):

        inv = 0
        if (l < r):
            mid = (l + r) // 2
            inv += self.mergeSort(arr, l, mid)
            inv += self.mergeSort(arr, mid + 1, r)
            inv += self.merge(arr, l, mid, r)

        return inv

    def merge(self, arr, l, mid, r):
        inv = 0
        n1 = mid - l + 1
        n2 = r - mid

        a = [None] * (n1)
        b = [None] * (n2)

        for i in range(n1):
            a[i] = arr[l + i]
        for i in range(n2):
            b[i] = arr[mid + i + 1]

        i, j, k = 0, 0, l

        while (i < n1 and j < n2):
            if a[i] <= b[j]:
                arr[k] = a[i]
                k += 1
                i += 1
            else:
                arr[k] = b[j]
                inv += n1 - i

                k += 1
                j += 1

        while (i < n1):
            arr[k] = a[i]
            k += 1
            i += 1
        while (j < n2):
            arr[k] = b[j]
            k += 1
            j += 1
        return inv

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    obj = Solution()
    print(obj.inversionCount(a, n))
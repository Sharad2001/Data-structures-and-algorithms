class Solution:
    def searchInsertK(self, Arr, N, k):
        for i in range(N):
            if Arr[i] == k:
                return i
            if Arr[i] != k:
                Arr.append(k)
                arr1 = sorted(Arr)
                return arr1.index(k)

if __name__ == '__main__':
    N = int(input())
    Arr = input().split()
    for itr in range(N):
        Arr[itr] = int(Arr[itr])
    k = int(input())
    ob = Solution()
    print(ob.searchInsertK(Arr, N, k))
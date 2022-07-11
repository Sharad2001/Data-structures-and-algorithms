class Solution:
    def maxSubarrayXOR(self, arr, N):
        INT_BITS = 32
        index = 0
        for i in range(INT_BITS - 1, -1, -1):
            maxInd = index
            maxEle = -2147483648
            for j in range(index, N):
                if ((arr[j] & (1 << i)) != 0 and arr[j] > maxEle):
                    maxEle = arr[j]
                    maxInd = j
            if (maxEle == -2147483648):
                continue
            temp = arr[index]
            arr[index] = arr[maxInd]
            arr[maxInd] = temp
            maxInd = index

            for j in range(N):
                if (j != maxInd and (arr[j] & (1 << i)) != 0):
                    arr[j] = arr[j] ^ arr[maxInd]
            index = index + 1
        res = 0
        for i in range(N):
            res = res ^ arr[i]
        return res

if __name__ == '__main__':
    n = int(input())
    set = list(map(int, input().split()))
    obj = Solution()
    print(obj.maxSubarrayXOR(set, n))
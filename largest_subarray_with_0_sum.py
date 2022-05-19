class Solution:
    def maxLen(self, n, arr):
        d = dict()
        suma = 0
        maxi = 0
        for i in range(n):
            suma += arr[i]

            if suma == 0:
                maxi = i + 1
                continue
            if suma not in d:
                d[suma] = i
            else:
                if i - d[suma] > maxi:
                    maxi = i - d[suma]
        return maxi

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.maxLen(n, arr))
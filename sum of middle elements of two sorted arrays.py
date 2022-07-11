class Solution:
    def findMidSum(self, ar1, ar2, n):
        i = 0
        j = 0
        count = 0
        sum = 0
        if n == 1:
            return ar1[0]+ ar2[0]
        if n == 2:
            return max(ar1[0], ar2[0])+min(ar1[1], ar2[1])
        while (i < n-1 and j < n-1):
            if ar1[i] <= ar2[j]:
                count += 1
                if count == n:
                    sum = ar1[i]
                    sum = sum + ar1[i+1] if ar1[i+1] <= ar2[j] else sum + ar2[j]
                    return sum
                i += 1
            if ar1[i] > ar2[j]:
                count += 1
                if count == n:
                    sum = ar2[j]
                    sum = sum + ar2[j+1] if ar2[j+1] < ar1[i] else sum+ar1[i]
                    return sum
                j += 1
        return sum

if __name__ == "__main__":
    n=int(input())
    ar1=list(map(int, input().strip().split()))
    ar2=list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.findMidSum(ar1, ar2, n)
    print(ans)
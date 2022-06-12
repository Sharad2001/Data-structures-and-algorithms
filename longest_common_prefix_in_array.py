class Solution:
    def longestCommonPrefix(self, arr, n):
        ans = []
        arr.sort()
        first = arr[0]
        last = arr[-1]
        for i in range(len(first)):
            if first[i] == last[i]:
                ans.append(first[i])
            else:
                break
        if ans:
            return (''.join(ans))
        return -1

if __name__ == '__main__':
    n = int(input())
    arr = [x for x in input().strip().split(" ")]

    ob = Solution()
    print(ob.longestCommonPrefix(arr, n))
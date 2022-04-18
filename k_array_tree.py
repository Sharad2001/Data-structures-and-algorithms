class Solution:
    def karyTree(self, k, m):

        return pow(k, m, 1000000007)

if __name__ == '__main__':
    k, m = map(int, input().split())

    ob = Solution()
    print(ob.karyTree(k, m))
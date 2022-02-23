class Solution:
    def factorial(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return n
        else:
            a = self.factorial(n - 1)
            return n * a
if __name__ == '__main__':
    n = int(input())
    ob = Solution()
    print(ob.factorial(n))

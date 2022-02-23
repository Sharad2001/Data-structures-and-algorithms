class Solution:
    def fibo(self, n):
        self.n = n
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            return self.fibo(n-1) + self.fibo(n-2)

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    ob = Solution()
    print(ob.fibo(n))
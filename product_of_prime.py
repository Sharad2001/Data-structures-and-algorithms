class Solution:
    def isPrime(self, n):
        limit = int(n ** 0.5)
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, limit + 1, 2):
            if n % i == 0:
                return False
        return True

    def primeProduct(self, L, R):
        prod = 1
        if L <= 2:
            prod = 2
        if L % 2 == 0:
            L += 1
        for i in range(L, R + 1, 2):
            if not self.isPrime(i):
                continue
            prod = prod * i
        return prod % 1000000007

if __name__ == '__main__':
    L, R = [int(x) for x in input().split()]

    ob = Solution()
    print(ob.primeProduct(L, R))
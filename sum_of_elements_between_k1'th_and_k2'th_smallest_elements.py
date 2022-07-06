class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        l = sorted(A)
        sum = 0
        for i in range(K1, K2-1):
            sum = sum + l[i]
        return sum


def main():
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    sz = [int(x) for x in input().strip().split()]
    k1, k2 = sz[0], sz[1]
    ob=Solution()
    print( ob.sumBetweenTwoKth(a, n, k1, k2) )


if __name__ == "__main__":
    main()
class Solution:
    def minValue(self, a, b, n):
        a.sort()
        b.sort()
        sum = 0
        for i in range(0, n):
            sum += a[i] * b[n-i-1]
        return sum

def main():
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    b = [int(x) for x in input().strip().split()]
    ob=Solution()
    print(ob.minValue(a, b, n))



if __name__ == "__main__":
    main()

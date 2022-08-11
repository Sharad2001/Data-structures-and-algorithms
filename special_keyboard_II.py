class Solution:
    def optimalKeys(self, N):
        if (N <= 6):
            return N

        screen = [0] * N
        for n in range(1, 7):
            screen[n - 1] = n
        for n in range(7, N + 1):
            screen[n - 1] = 0

            for b in range(n - 3, 0, -1):
                curr = (n - b - 1) * screen[b - 1]
                if (curr > screen[n - 1]):
                    screen[n - 1] = curr
        return screen[N - 1]


if __name__ == '__main__':
    N = int(input())

    ob = Solution()
    print(ob.optimalKeys(N))
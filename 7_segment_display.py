class Solution:
    def sevenSegments(self, S, N):
        seg = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]
        count = sum(seg[int(ch)] for ch in S[:N])
        ans = ""
        lower = 2 * N
        upper = 7 * N
        for _ in range(N):
            lower -= 2
            upper -= 7
            for i in [0, 1, 2, 4, 7, 8]:
                remain = count - seg[i]
                if remain >= lower and remain <= upper:
                    ans += str(i)
                    count = remain
                    break
        return ans

if __name__ == '__main__':
    N = int(input())
    S = input()

    ob = Solution()
    print(ob.sevenSegments(S, N))

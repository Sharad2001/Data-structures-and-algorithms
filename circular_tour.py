'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''
class Solution:

    def tour(self, lis, n):
        start = 0
        s = 0
        d = 0
        for i in range(n):
            s += lis[i][0] - lis[i][1]
            if s < 0:
                start = i + 1
                d += s
                s = 0
        return start if (s + d) >= 0 else -1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = []
    for i in range(1, 2 * n, 2):
        lis.append([arr[i - 1], arr[i]])
    print(Solution().tour(lis, n))
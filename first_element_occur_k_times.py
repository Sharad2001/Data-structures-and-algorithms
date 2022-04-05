class Solution:
    def firstElementKTime(self, a, n, k):
        from collections import defaultdict

        freq_map = defaultdict(int)
        for i in a:
            freq_map[i] += 1
            if freq_map[i] == k:
                return i
        return -1

def main():
    sz = [int(x) for x in input().strip().split()]
    n, k = sz[0], sz[1]
    a = [int(x) for x in input().strip().split()]
    ob = Solution()
    print(ob.firstElementKTime(a, n, k))

if __name__ == '__main__':
    main()
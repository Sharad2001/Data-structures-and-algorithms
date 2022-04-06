class Solution:

    def max_non_overlapping(self, ranges):
        ranges.sort(key=lambda x: x[1])

        prev = -1
        count = 0
        for i in range(n):
            if ranges[i][0] >= prev:
                count += 1
                prev = ranges[i][1]
        return count

if __name__ == '__main__':
    n = int(input())
    line = input().strip().split()
    ranges = [[] for j in range(n)]
    j = 0
    for i in range(0, 2 * n, 2):
        ranges[j].append(int(line[i]))
        ranges[j].append(int(line[i + 1]))
        j += 1

    obj = Solution()
    print(obj.max_non_overlapping(ranges))
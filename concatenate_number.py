class Solution:
    def countPairs(self, N, X, numbers):

        count = 0
        dic = {}
        for i in numbers:
            if str(i) in dic:
                dic[str(i)] += 1
            else:
                dic[str(i)] = 1
        no = str(X)
        for i in range(len(no)):
            s1 = no[:i + 1]
            s2 = no[i + 1:]

            if s1 in dic and s2 in dic:
                if s1 == s2:
                    count += (dic[s1] * (dic[s2] - 1))
                else:
                    count += (dic[s1] * dic[s2])

        return count

if __name__ == '__main__':
    N, X = map(int, input().strip().split())
    numbers = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.countPairs(N, X, numbers)
    print(ans)

class Solution:
    def stringPartition(ob, S, a, b):
        res = ""
        for i in range(1, len(S)):
            if int(S[:i]) % a == 0 and int(S[i:]) % b == 0:
                return S[:i] + " " + S[i:]
        return -1

if __name__ == '__main__':
    S, a, b = map(str, input().strip().split(" "))
    a = int(a)
    b = int(b)
    ob = Solution()
    print(ob.stringPartition(S, a, b))
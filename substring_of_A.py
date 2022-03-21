class Solution:
    def minRepeats(self, A, B):
        for i in B:
            if i not in A:
                return -1
        for i in A:

            if i not in B:
                return -1

        op = 0
        s = ""
        while len(s) < len(B):
            s += A
            op += 1

        if s.find(B) != -1:
            return op

        s += A
        op += 1
        if s.find(B) != -1:
            return op

        return -1

if __name__ == '__main__':
    A = input()
    B = input()

    ob = Solution()
    print(ob.minRepeats(A, B))
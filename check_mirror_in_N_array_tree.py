class Solution:
    def checkMirrorTree(self, n, e, A, B):
        tree1 = {}
        tree2 = {}
        for i in range(0, (2 * e), 2):
            if A[i] not in tree1:
                tree1[A[i]] = [A[i + 1]]
            else:
                tree1[A[i]] += [A[i + 1]]
            if B[i] not in tree2:
                tree2[B[i]] = [B[i + 1]]
            else:
                tree2[B[i]] += [B[i + 1]]
        for i in tree1.keys():
            if tree1[i] != tree2[i][::-1]:
                return 0
        return 1

if __name__ == '__main__':
    n, e = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ob = Solution()
    print(ob.checkMirrorTree(n, e, A, B))

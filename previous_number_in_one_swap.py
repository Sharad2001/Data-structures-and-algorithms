class Solution:
    def lower_bound(ob, A, i):
        m = -1
        k = 0
        for j in range(i, len(A)):
            if A[i - 1] > A[j]:
                if m < int(A[j]):
                    m = int(A[j])
                    k = j
        return k

    def previousNumber(ob, S):
        A = list(S)
        t = 0
        d = 0
        for i in range(len(S) - 1, 0, -1):
            if A[i] < A[i - 1]:
                t = ob.lower_bound(A, i)
                A[t], A[i - 1] = A[i - 1], A[t]
                break
        r = "".join(A)
        if S == r or r[0] == "0":
            return -1
        else:
            return r

if __name__ == '__main__':
    S = str(input())

    ob = Solution()
    print(ob.previousNumber(S))
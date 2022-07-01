class Solution:
    def knows(self, M, a, b):
        if M[a][b] == 1:
            return True

    def celebrity(self, M, n):
        stack = []
        for i in range(n):
            stack.append(i)
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if self.knows(M, a, b):
                stack.append(b)
            else:
                stack.append(a)
        celeb = stack[-1]
        for i in range(n):
            if M[celeb][i] == 1 or M[i][celeb] == 0 and i != celeb:
                return -1
        return celeb

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    k = 0
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(a[k])
            k += 1
        m.append(row)
    ob = Solution()
    print(ob.celebrity(m, n))
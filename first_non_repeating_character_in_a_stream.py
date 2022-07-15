class Solution:
    def FirstNonRepeating(self, A):
        flag = [0]*26
        q = []
        ans = []
        for v in A:
            i = ord(v) - ord('a')
            flag[i] += 1
            if flag[i] == 1:
                q.append(v)
            if flag[i] == 2:
                q.remove(v)
            ans.append(q[0] if q else '#')
        return ''.join(ans)

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)
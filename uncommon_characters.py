class Solution:
    def UncommonChars(self,A, B):
        #code here
        A = list(A)
        B = list(B)
        arr = []
        for i in B:
            if i not in A:
                arr.append(i)
        for i in A:
            if i not in B:
                arr.append(i)
        if len(arr) == 0:
            return -1
        y = set(arr)
        y = list(y)
        y.sort()
        x = "".join(map(str, y))
        return x

if __name__ == '__main__':
    A = input()
    B = input()
    ob = Solution()
    print(ob.UncommonChars(A, B))
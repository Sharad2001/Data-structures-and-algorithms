class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        res = []
        i = 0
        j = 0
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        while i < n:
            res.append(arr1[i])
            i += 1
        while j < m:
            res.append(arr2[j])
            j += 1
        return res[k - 1]


def main():
    sz = [int(x) for x in input().strip().split()]
    n, m, k = sz[0], sz[1], sz[2]
    a = [int(x) for x in input().strip().split()]
    b = [int(x) for x in input().strip().split()]
    ob = Solution()
    print(ob.kthElement(a, b, n, m, k))

if __name__ == "__main__":
    main()
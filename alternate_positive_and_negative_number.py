class Solution:
    def rearrange(self,arr, n):
        neg = []
        pos = []
        for i in range(0, n):
            if arr[i] < 0:
                neg.append(arr[i])
            else:
                pos.append(arr[i])
        i, j = 0, 0
        a = []
        while i < len(pos) or j < len(neg):
            if i == len(pos):
                a.append(neg[j])
                j += 1
            elif j == len(neg):
                a.append(pos[i])
                i += 1
            else:
                if len(a) == 0 or a[-1] < 0:
                    a.append(pos[i])
                    i += 1
                else:
                    a.append(neg[j])
                    j += 1
        for i in range(n):
            arr[i] =  a[i]

if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().strip().split()))
	ob = Solution()
	ob.rearrange(arr, n)
	for x in arr:
		print(x, end=" ")
	print()
def reaching_height(n, arr):
    currLevel = 0
    if n == 1:
        return [arr[0]]
    arr.sort()
    ans = []
    i, j = n - 1, 0
    while j <= i:
        if i == j:
            ans.append(arr[i])
            currLevel += arr[i]
            break
        ans.append(arr[i])
        ans.append(arr[j])
        currLevel -= arr[i]
        currLevel += arr[j]
        if currLevel == 0:
            return [-1]
        i -= 1
        j += 1
    return ans

n = int(input())
arr = list(map(int, input().strip().split()))
ans = reaching_height(n, arr)
if (len(ans) == 1 and ans[0] == -1):
    print("Not Possible")
else:
    print(*ans)
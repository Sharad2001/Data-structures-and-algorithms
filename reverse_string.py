def reverseString(s):
    low = 0
    high = len(s)-1
    while low < high:
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1
    return s
if __name__ == '__main__':
    s = list(map(str, input().split()))
    print(reverseString(s))
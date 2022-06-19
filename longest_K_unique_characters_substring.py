class Solution:

    def longestKSubstr(self, s, k):
        # code here
        l = 0
        h = 0
        hmap = {}
        while (h < len(s) and len(hmap) <= k):
            if s[h] not in hmap:
                hmap[s[h]] = 1
            elif s[h] in hmap:
                hmap[s[h]] += 1
            h += 1
        h -= 1
        if h < len(s) - 1:
            if hmap[s[h]] > 1:
                hmap[s[h]] -= 1
            else:
                hmap.pop(s[h])
            maxlen = h
        elif h == len(s) - 1:
            maxlen = h
        if len(hmap) < k:
            return -1
        # print(hmap,maxlen)
        while (h < len(s)):
            # print(hmap,h,l)
            if len(hmap) > k:
                while (l <= h and len(hmap) > k):
                    if s[l] in hmap and hmap[s[l]] > 1:
                        hmap[s[l]] -= 1
                    elif s[l] in hmap and hmap[s[l]] <= 1:

                        hmap.pop(s[l])
                    l += 1

            if s[h] in hmap:
                hmap[s[h]] += 1
            else:
                hmap[s[h]] = 1
            if len(hmap) == k:
                maxlen = max(maxlen, h - l + 1)
            h += 1
        return maxlen

if __name__ == '__main__':
    s = input()
    k = int(input())
    solObj = Solution()
    ans = solObj.longestKSubstr(s, k)
    print(ans)
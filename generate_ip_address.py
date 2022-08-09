class Solution:
    def is_valid(self, ip):
        ip = ip.split(".")

        for i in ip:
            if (len(i) > 3 or int(i) < 0 or int(i) > 255):
                return False
            if (len(i) > 1 and int(i) == 0):
                return False
            if (len(i) > 1 and int(i) != 0 and i[0] == '0'):
                return False
        return True

    def genIp(self, s):
        sz = len(s)
        if sz > 12:
            return []

        snew = s
        l = []
        for i in range(1, sz - 2):
            for j in range(i + 1, sz - 1):
                for k in range(j + 1, sz):
                    snew = snew[:k] + "." + snew[k:]
                    snew = snew[:j] + "." + snew[j:]
                    snew = snew[:i] + "." + snew[i:]

                    if self.is_valid(snew):
                        l.append(snew)
                    snew = s
        return l

if __name__ == '__main__':
    s = input().strip()
    res = Solution().genIp(s)
    res.sort()
    if (len(res)):
        for u in res:
            print(u)
    else:
        print(-1)
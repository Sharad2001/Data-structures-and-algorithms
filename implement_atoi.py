class Solution:
    def atoi(self,string):
        res, count = 0, 0
        for char in string:
            if char == "-":
                count += 1
                if count > 1 or res > 0:
                    return -1
                continue
            if not char.isnumeric():
                return -1
            res = res*10+(ord(char)-48)
        if count == 1:
            return -res
        else:
            return res

if __name__=='__main__':
    string = input().strip();
    ob=Solution()
    print(ob.atoi(string))
class Solution:
    def remove(self, S):
        global string
        string = S
        sub = ""
        skip = False
        dupfound = False
        for i in range(0, len(string)):
            if i == len(string) - 1:
                if not skip:
                    sub += string[i]
            else:
                if skip:
                    if string[i] != string[i + 1]:
                        skip = False
                else:
                    if string[i] == string[i + 1]:
                        skip = True
                        dupfound = True
                    else:
                        sub += string[i]
        string = sub
        if dupfound:
            self.remove(string)
        return string

if __name__ == '__main__':
    S = input()
    ob = Solution()
    print(ob.remove(S))
class Solution:
    def findIndex(self,str):
        n = len(str)
        for i in str:
            if i == "(":
                n -= 1
        return n

def main():
    str = input()
    ob=Solution()
    print(ob.findIndex(str))

if __name__ == "__main__":
    main()
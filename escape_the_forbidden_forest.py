class Solution:
    def build_bridges(self, str1, str2):
        matrix = [[0 for j in range(len(str2) + 1)] for i in range(len(str1)+1)]
        for i in range(len(str1)-1, -1, -1):
            for j in range(len(str2)-1, -1, -1):
                if str1[i] == str2[j]:
                    matrix[i][j] = 1 + matrix[i+1][j+1]
                else:
                    matrix[i][j] = max(matrix[i+1][j], matrix[i][j+1])
        return matrix[0][0]
if __name__ == '__main__':
    obj = Solution()
    str1, str2 = input().split()
    print(obj.build_bridges(str1, str2))

def kthSmallest(mat, n, k):
    index = 0
    matrix = [0] * (n * n)
    for i in range(n):
        for j in range(n):
            matrix[index] = mat[i][j]
            index += 1
    matrix.sort()
    ans = matrix[k - 1]
    return ans

def main():
    n = int(input())
    mat = [[0 for j in range(n)] for i in range(n)]
    line1 = [int(x) for x in input().strip().split()]
    k = int(input())

    temp = 0
    for i in range(n):
        for j in range(n):
            mat[i][j] = line1[temp]
            temp += 1

    print(kthSmallest(mat, n, k))


if __name__ == "__main__":
    main()
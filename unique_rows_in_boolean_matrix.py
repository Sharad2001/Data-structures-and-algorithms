def uniqueRow(row, col, matrix):
    l = []
    l2 = []
    k = 0
    for i in range(row):
        l.append(matrix[k:k + col])
        k += col
    for j in l:
        if j not in l2:
            l2.append(j)
    return l2

def main():
    s = input().split()
    row = int(s[0])
    col = int(s[1])
    matrix = input().split()

    a = uniqueRow(row, col, matrix)

    for row in a:
        for value in row:
            print(value, end=" ")
        print("$", end="")
    print()

if __name__ == "__main__":
    main()
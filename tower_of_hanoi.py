def TOH(n, A, B, C):
    if n == 1:
        print("Move 1 from", A, "to", C)
    else:
        TOH(n-1, A, B, C)
        print("Move", n, "from", A, "to", C)
        TOH(n-1, B, A, C)
TOH(int(input("Enter the number of disc: ")), "A", "B", "C")
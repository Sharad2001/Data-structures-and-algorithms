def theSequence(n):
    if n == 0:
        return 1
    else:
        return n + n * (theSequence(n - 1))

if __name__ == '__main__':
    n = int(input("Enter the value of n: "))

    print(theSequence(n))

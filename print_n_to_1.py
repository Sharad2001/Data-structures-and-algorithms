def f(n):
    if n <= 0:
        return
    print(n)
    f(n-1)

n = int(input("Enter the number: "))
f(n)
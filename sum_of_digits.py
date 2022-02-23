def f(n):
  if n < 10:
    return n
  return f(n // 10) + n%10
n = int(input("Enter the number: "))
print(f(n))

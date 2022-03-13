import math
def num(n):
    count = 0
    product = 1
    for i in range(n + 1):
        powe = i ** 4
        rem = i % 10
        product = product * rem
        i = i // 10
        if math.gcd(powe, product) > 1:
            count += 1

    return count

# n = int(input(101))

print(num(101))
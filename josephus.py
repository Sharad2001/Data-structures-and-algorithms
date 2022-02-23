def jos(n, k):
    if n == 0:
        return 0
    else:
        return (jos(n-1, k) + k)%n

def josBeginWithOne(n, k):
    return jos(n, k) + 1

print(josBeginWithOne(4, 2))
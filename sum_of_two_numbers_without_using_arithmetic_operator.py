def sum(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

import math
def main():
    inp = list(map(int, input().split()))

    a = inp[0]
    b = inp[1]
    print(sum(a, b))

if __name__ == "__main__":
    main()
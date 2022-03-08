def sumOfProductOfDigits(n1, n2):
    sum1 = 0
    while (n1 > 0 and n2 > 0):
        sum1 += ((n1%10)*(n2%10))
        n1 = n1 // 10
        n2 = n2 // 10
    return sum1

if __name__ == "__main__":
    n1_n2 = [int(x) for x in input().strip().split()]
    n1 = n1_n2[0]
    n2 = n1_n2[1]
    print(sumOfProductOfDigits(n1, n2))
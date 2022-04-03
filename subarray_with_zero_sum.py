def isZeroSum(l):
    pre_sum = 0
    h = set()
    for i in range(0, len(l)):
        pre_sum += l[i]
        if pre_sum == 0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False

l = list(map(int, input().strip().split()))
print(isZeroSum(l))
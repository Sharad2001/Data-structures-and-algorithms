def distinctElement(l):
    res = 0
    for i in range(0, len(l)):
        if l[i] not in l[0:i]:
            res = res+1
    return res

l = list(map(int, input().strip().split()))
print(f"Actual length of the list is: {len(l)}")
print(f"Legth of list using distinct element is: {distinctElement(l)}")
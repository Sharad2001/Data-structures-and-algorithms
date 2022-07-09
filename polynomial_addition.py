class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, coeff, pwr):
        if self.head == None:
            self.head = node(coeff, pwr)
        else:
            new_node = node(coeff, pwr)
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    k = 0
    for i in range(n):
        lis.insert(arr[k], arr[k + 1])
        k += 2
    return lis.head

class Solution:
    def addPolynomial(self, poly1, poly2):
        maxPoly = None
        minPoly = None
        resPoly = node(-1, -1)
        temp = resPoly

        while (poly1 and poly2):
            if (poly1.power == poly2.power):
                temp.next = node(poly1.coef + poly2.coef, poly1.power)
                temp = temp.next
                poly1 = poly1.next
                poly2 = poly2.next

            elif (poly1.power > poly2.power):
                temp.next = node(poly1.coef, poly1.power)
                temp = temp.next
                poly1 = poly1.next
            else:
                temp.next = node(poly2.coef, poly2.power)
                temp = temp.next
                poly2 = poly2.next

        while (poly1):
            temp.next = node(poly1.coef, poly1.power)
            temmp = temp.next
            poly1 = poly1.next

        while (poly2):
            temp.next = node(poly2.coef, poly2.power)
            temp = temp.next
            poly2 = poly2.next
        return resPoly.next

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    poly1 = createList(arr, n)
    n = int(input())
    arr = list(map(int, input().strip().split()))
    poly2 = createList(arr, n)
    sum = Solution().addPolynomial(poly1, poly2)
    ptr = sum
    while ptr is not None:
        print(str(ptr.coef) + 'x^' + str(ptr.power), end='')
        ptr = ptr.next
        if ptr is not None:
            print(' +', end=' ')
    print()
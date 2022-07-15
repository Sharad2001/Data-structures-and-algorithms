from collections import OrderedDict

class LRUCache:

    def __init__(self, cap):
        self.cap = cap
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=True)
        else:
            self.cache[key] = value
            if len(self.cache) > self.cap:
                self.cache.popitem(last=False)


if __name__ == '__main__':
    cap = int(input())
    qry = int(input())
    a = list(map(str, input().strip().split()))

    lru = LRUCache(cap)

    i = 0
    q = 1
    while q <= qry:
        qtyp = a[i]

        if qtyp == 'SET':
            lru.set(int(a[i + 1]), int(a[i + 2]))
            i += 3
        elif qtyp == 'GET':
            print(lru.get(int(a[i + 1])), end=' ')
            i += 2
        q += 1
    print()
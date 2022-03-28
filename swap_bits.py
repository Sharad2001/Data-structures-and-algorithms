class Solution:
    def swapBits(self, X, P1, P2, N):
        # Move all bits of first
        # set to rightmost side
        set1 = (X >> P1) & ((1 << N) - 1)

        # Move all bits of second
        # set to rightmost side
        set2 = (X >> P2) & ((1 << N) - 1)

        # XOR two sets
        xor = (set1 ^ set2)

        # Put xor bits to the original
        # Position
        xor = (xor << P1) | (xor << P2)
        result = X ^ xor
        return result

if __name__ == '__main__':
    obj = Solution()
    X, P1, P2, N = map(int, input().split())
    print(obj.swapBits(X, P1, P2, N))

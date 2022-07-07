class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

class NumsNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

def main():
    x = NumsNode(5)
    y = NumsNode(4)
    p = PlusNode(x, y)
    t = TimesNode(p, NumsNode(6))
    root = PlusNode(t, NumsNode(3))
    print(root.eval())

if __name__ == "__main__":
    main()
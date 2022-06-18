def isValid(s):
    if '..' in s or s.count('.') > 3 or s.count('.') < 3:
        return False
    t = s.split(".")
    if len(t) > 4 or len(t) < 4:
        return False
    for i in t:
        if i.isalpha():
            return False
        if i != str(int(i)):
            return False
        if int(i) not in range(0, 256):
            return False
    return True

if __name__ == "__main__":
    s = input()
    if (isValid(s)):
        print(1)
    else:
        print(0)
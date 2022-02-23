def sol():
    s = input()
    res = 1
    for i in range(0, len(s)):
        mid = i
        r = 1
        while mid + r < len(s) and mid - r >= 0 and s[mid + r] == s[mid - r]:
            res = max(res, r * 2 + 1)
            r += 1

    for i in range(0, len(s) - 1):
        mid1 = i
        mid2 = i + 1
        r = 0
        while mid1 - r >= 0 and mid2 + r < len(s) and s[mid1 - r] == s[mid2 + r]:
            res = max(res, r * 2 + 2)
            r += 1

    print(res)


if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        sol()

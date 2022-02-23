def sol():
    n = int(input())
    a, b = map(int, input().split())
    cur = 0
    x = 1
    z = []
    for i in range(n-2):
        c, d = map(int, input().split())
        if c == a or c == b:
            cur = c
            z.append(d)
        elif d == a or d == b:
            cur = d
            z.append(c)
        else:
            x = 0
    if len(set(z)) != n - 2:
        x = 0
    if x == 0:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    sol()

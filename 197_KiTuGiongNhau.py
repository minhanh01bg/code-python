def sol():
    n = int(input())
    x = [int(i) for i in input().split()]
    while len(x) < 3:
        x.extend([int(i) for i in input().split()])
    a = x[0]
    b = x[1]
    c = x[2]
    f = [0]*(n + 1)
    f[0] = 0
    f[1] = a
    
    for i in range(2, n + 1):
        if i % 2 == 0:
            f[i] = min(f[i - 1] + a, f[int(i / 2)] + c)
        else:
            f[i] = min(f[i - 1] + a, min(f[int(i/2) + 1] +
                       b + c, f[int(i / 2)] + a + c))

    print(f[n])

if __name__ == "__main__":
    for i in range(int(input())):
        sol()

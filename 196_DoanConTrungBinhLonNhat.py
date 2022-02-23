
def sol():
    n = int(input())
    a = [int(i) for i in input().split()]
    maxdouble = 0
    for i in range(0, n-1):
        if (a[i] + a[i+1])//2 > maxdouble:
            maxdouble = (a[i] + a[i + 1]) // 2
    ans = 2
    cur = 0
    for i in range(n):
        if a[i] >= maxdouble:
            cur += 1
            if ans < cur:
                ans = cur
        else:
            cur = 0
    print(ans)


if __name__ == '__main__':
    sol()

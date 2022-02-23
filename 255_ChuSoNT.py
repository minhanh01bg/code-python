val = [0, 2, 3, 5, 7]


def Try(i, n, a, check):
    for j in range(1, 5):
        a[i] = j
        if i == n-1:
            if val[a[n-1]] != 2:
                b = []
                for i in range(n):
                    b.append(a[i])
                if len(set(b)) == 4:
                    for i in range(n):
                        print(val[a[i]], end="")
                    print()
        else:
            Try(i+1, n, a, check)


if __name__ == '__main__':
    m = int(input())
    n = 4
    while n <= m:
        a = [0]*n
        check = [0]*5
        Try(0, n, a, check)
        n += 1

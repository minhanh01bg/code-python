def sol():
    n = int(input())
    a = [int(i) for i in input().split()]
    i = 0
    j = i+1
    y = 1
    while True:
        x = 1

        if len(a) == 1 or len(a) == 0:
            break

        if (a[i] + a[j]) % 2 == 0:
            # print(a[i], a[j])
            a.pop(j)
            a.pop(i)
            x = 0
            y = 0

        if i > 0 and y == 0:
            i -= 1
            j = i+1
            y = 1
            x = 0
        else:
            i += 1
            j = i+1
            x = 0
        if x == 1 or j >= len(a) or i >= len(a):
            break

    # for i in range(0, len(a)):
    #     print(a[i], end=" ")
    print(len(a))


if __name__ == '__main__':
    sol()

def sol():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    x = a[0]*a[1]*a[-1]
    x = max(x, a[0]*a[1]*a[2])
    x = max(x, a[0]*a[-1]*a[-2])
    x = max(x, a[-1]*a[-2]*a[-3])
    print(x)

if __name__ == '__main__':
    sol()

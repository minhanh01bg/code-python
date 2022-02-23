def sol():
    n = int(input())
    a = [int(i) for i in input().split()]
    min1 = max(a)
    x = 0
    for i in range(n):
        if a[i] < min1:
            min1 = a[i]
            x = i

    min2 = max(a)
    y = 0
    for i in range(n):
        if a[i] >= min1 and a[i] < min2 and i != x:
            min2 = a[i]
            y = i
    min3 = max(a)
    for i in range(n):
        if a[i] >= min2 and a[i] < min3 and i != y:
            min3 = a[i]
    print(str(min1+min2+min3))


for i in range(int(input())):
    sol()

'''
2
7
1 2 3 0 -1 8 10 
7
9 8 20 3 4 -1 0
'''

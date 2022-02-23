import math


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


p = pow(10, 9) + 7

if __name__ == "__main__":
    test = int(input())
    while test != 0:
        test -= 1
        n, r = map(int, input().split())
        if r > n:
            print(0)
        else:
            print(int(nCr(n, r) % p))

import math
import bisect


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def sol():
    n = int(input())
    # a = []
    # sàng số nguyên tố
    check = [0] * 16000
    a = []
    for i in range(2, 16000):
        if check[i] == 0:
            a.append(i)
            for j in range(i * i, 16000, i):
                check[j] = 1

    cnt = 0
    for i in range(len(a)):
        x = bisect.bisect_left(a, int(math.sqrt(n//(a[i]**2)))+1) # lower_bound
        if x - i > 0 and x < len(a):
            cnt += (x - i - 1)
        if a[i]**8 <= n:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    sol()

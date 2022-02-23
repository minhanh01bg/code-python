import math
import re


def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1


def sol():
    n = int(input())
    a = [int(i) for i in input().split()]
    dic = {}
    for i in range(n):
        if a[i] not in dic:
            dic[a[i]] = 1
        else:
            dic[a[i]] += 1

    b = []
    sum = 0
    for i in range(n):
        if dic[a[i]] != 0:
            sum += a[i]
            b.append(a[i])
            dic[a[i]] = 0
    cur = b[0]
    for i in range(1, len(b)):
        if isPrime(cur) and isPrime(sum - cur):
            print(i - 1)
            return
        cur += b[i]
    print("NOT FOUND")


if __name__ == "__main__":
    sol()

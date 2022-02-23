#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-11 22:21:39
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os


def sol():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = [0] * n
    d[0] = a[0]
    for i in range(1, n):
        d[i] = d[i - 1] + a[i]
    b = []
    for i in range(0, n):
        b.append(a[i])
    b.sort()

    d1 = [0] * n
    d1[0] = b[0]
    for i in range(1, n):
        d1[i] = d1[i - 1] + b[i]
    # for i in range(0, n):
    #     print(d[i], end=" ")
    # print()

    # for i in range(0, n):
    #     print(d1[i], end=" ")
    # print()
    cnt = 0

    for i in range(0, n - 1):
        if a[i] == b[i] and d1[i] == d[i] and a[i + 1] != a[i]:
            cnt = cnt + 1
    if a[n - 1] == b[n - 1]:
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    for i in range(int(input())):
        sol()

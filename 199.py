#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-10 21:14:59
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os


def sol():
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    cnt = 1
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) > k:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    sol()

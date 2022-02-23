#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-10 14:04:40
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os


def sol():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0]*30011
    for i in range(n):
        if b[a[i]] == 0:
            b[a[i]] = 1

    for i in range(1,max(a)+1):
        if b[i] == 0:
            return i
    return max(a) + 1

if __name__ == "__main__":
    print(sol())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-08 22:44:20
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os
import math


def sol():
    a = input().strip()
    b = []
    for i in range(len(a)):
        b.append(ord(a[i])-48)
    
    b.reverse()
    for i in range(len(b) - 1):
        if b[i] >= 5:
            b[i] = 0
            b[i + 1] += 1
        else:
            b[i] = 0
    b.reverse()
    for i in range(len(b)):
        print(b[i],end="")
    print()

if __name__ == "__main__":
    test = int(input())
    while test != 0:
        test -= 1
        sol()

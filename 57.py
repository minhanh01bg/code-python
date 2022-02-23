#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-10 20:57:26
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os


def sol():
    n = int(input())
    ans = 0
    if n & 1:
        for i in range(1,n+1):
            if i & 1:
                ans = ans + 1 / i
    else:
        for i in range(1,n+1):
            if i & 1 == False:
                ans += (1 / i)
    
    print("{:.6f}".format(ans))
    # print("%.6f" % ans)

if __name__ == "__main__":
    for i in range(int(input())):
        sol()

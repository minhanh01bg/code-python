#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-10 20:47:05
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os,math

def sol():
    n = input()
    nn = int("".join(reversed(n)))
    n = int(n)
    if math.gcd(n, nn) == 1:
        print("YES")
    else:
        print("NO")    
    
if __name__ == '__main__':
    for i in range(int(input())):
        sol()

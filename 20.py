#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-08 22:44:20
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os
import math


def check1(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    if n<=1: return False
    if n<=3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

def sol():
    n = int(input())
    a = [int(i) for i in input().split()]
    dic = {}
    for i in a:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for i in a:
        if check(i) and dic[i] != 0:
            print(str(i) + " " + str(dic[i]))
            dic[i] = 0


if __name__ == "__main__":
    # test = int(input())
    # while test != 0:
    # test -= 1
    sol()

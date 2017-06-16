#!/bin/python3

import sys


def run():
    x1, v1, x2, v2 = input().strip().split(' ')
    x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
    a = (x1, v1)
    b = (x2, v2)

    print("YES")

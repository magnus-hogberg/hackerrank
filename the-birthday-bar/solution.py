#!/bin/python3

import sys


def solve(n, s, d, m):
    r = 0
    for i in range(n - m + 1):
        sl = s[i:i+m]
        if sum(sl) == d:
            r += 1
    return r


if __name__ == "__main__":
    n = int(input().strip())
    s = list(map(int, input().strip().split(' ')))
    d, m = input().strip().split(' ')
    d, m = [int(d), int(m)]
    result = solve(n, s, d, m)
    print(result)
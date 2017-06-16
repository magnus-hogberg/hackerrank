#!/bin/python3

import sys


def get_record(scores):
    min = scores[0]
    max = scores[0]
    n_min = 0
    n_max = 0
    for score in scores:
        if score > max:
            max = score
            n_max += 1
        if score < min:
            min = score
            n_min += 1
    return [n_max, n_min]


if __name__ == "__main__":
    n = int(input().strip())
    s = list(map(int, input().strip().split(' ')))
    result = get_record(s)
    print(" ".join(map(str, result)))

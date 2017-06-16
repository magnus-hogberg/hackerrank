#!/bin/python3

def fruit_hits(tree, house, fruits):
    hits = 0
    for fruit in fruits:
        a_rel = tree + fruit
        if house[0] <= a_rel <= house[1]:
            hits += 1
    return hits

def run():
    s,t = input().strip().split(' ')
    s,t = [int(s), int(t)]
    a,b = input().strip().split(' ')
    a,b = [int(a), int(b)]
    m,n = input().strip().split(' ')
    m,n = [int(m), int(n)]
    apples = [int(apple_temp) for apple_temp in input().strip().split(' ')]
    oranges = [int(orange_temp) for orange_temp in input().strip().split(' ')]

    print(fruit_hits(a, (s, t), apples))
    print(fruit_hits(b, (s, t), oranges))

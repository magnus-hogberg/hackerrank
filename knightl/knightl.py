from collections import OrderedDict

def knightl_single(n, i, j):
    s = OrderedDict({(0, 0): 0})
    v = []
    while True:
        if len(s) == 0:
            return -1
        p, k = s.popitem(False)
        v.append(p)
        if p == (n-1, n-1):
            return k
        if p[0] + i < n and p[1] + j < n and (p[0]+i, p[1]+j) not in v and (p[0]+i, p[1]+j) not in s:
            s[(p[0]+i, p[1]+j)] = k+1
        if p[0] + j < n and p[1] + i < n and (p[0]+j, p[1]+i) not in v and (p[0]+j, p[1]+i) not in s:
            s[(p[0]+j, p[1]+i)] = k+1

        if p[0] + i < n and p[1] - j >= 0 and (p[0]+i, p[1]-j) not in v and (p[0]+i, p[1]-j) not in s:
            s[(p[0]+i, p[1]-j)] = k+1
        if p[0] + j < n and p[1] - i >= 0 and (p[0]+j, p[1]-i) not in v and (p[0]+j, p[1]-i) not in s:
            s[(p[0]+j, p[1]-i)] = k+1

        if p[0] - i >= 0 and p[1] + j < n and (p[0]-i, p[1]+j) not in v and (p[0]-i, p[1]+j) not in s:
            s[(p[0]-i, p[1]+j)] = k+1
        if p[0] - j >= 0 and p[1] + i < n and (p[0]-j, p[1]+i) not in v and (p[0]-j, p[1]+i) not in s:
            s[(p[0]-j, p[1]+i)] = k+1

        if p[0] - i >= 0 and p[1] - j >= 0 and (p[0]-i, p[1]-j) not in v and (p[0]-i, p[1]-j) not in s:
            s[(p[0]-i, p[1]-j)] = k+1
        if p[0] - j >= 0 and p[1] - i >= 0 and (p[0]-j, p[1]-i) not in v and (p[0]-j, p[1]-i) not in s:
            s[(p[0]-j, p[1]-i)] = k+1

        s = OrderedDict(sorted(s.items(), key=lambda x: x[1]))


def knightl(n):
    result = []
    for i in range(1, n):
        r = []
        for j in range(1, n):
            r.append(knightl_single(n, i, j))
        result.append(r)
    return result


if __name__ == "__main__":
    n = int(input().strip())
    result = knightl(n)
    for l in result:
        print(" ".join([str(i) for i in l]))

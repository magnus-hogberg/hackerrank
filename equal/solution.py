def search(colleagues):
    # i = 0
    # while not all(colleagues[0] == item for item in colleagues):
    #     i += 1
    #     m = max(colleagues)
    #     n = min(colleagues)
    #     if m - n >= 5:
    #         colleagues[colleagues.index(m)] -= 5
    #     elif 5 > m - n >= 2:
    #         colleagues[colleagues.index(m)] -= 2
    #     else:
    #         colleagues[colleagues.index(m)] -= 1
    # return i
    i = 0
    x = min(colleagues)
    for n in range(len(colleagues)):
        y = colleagues[n] - x
        i += int(y/5)
        y = y % 5
        i += int(y/2)
        y = y % 2
        i += y
    return i


if __name__ == "__main__":
    n_cases = input()
    l = input()
    col = map(int, input().split(" "))
    print(search(col))
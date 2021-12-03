def solve1(path) -> int:
    with open(path) as file:
        ll = file.readlines()
        ll = [l.rstrip() for l in ll]

    w = len(ll[0])
    g, e = 0, 0

    for p in range(0, w):
        c0, c1 = 0, 0
        for l in ll:
            c0 += l[p] == "0"
            c1 += l[p] == "1"
        if c1 > c0:
            g += 1 << (w - p - 1)
        else:
            e += 1 << (w - p - 1)

    # print(g, e)
    return e * g


def solve2(path) -> int:
    with open(path) as file:
        ll = file.readlines()
        ll = [l.rstrip() for l in ll]

    dd = ll
    w = len(ll[0])
    # oxygen
    for p in range(0, w):
        c0, c1 = 0, 0
        mark = -1
        for l in ll:
            c0 += l[p] == "0"
            c1 += l[p] == "1"
        if c1 >= c0:
            mark = "1"
        else:
            mark = "0"
        tmp = []
        for l in ll:
            if l[p] == mark:
                tmp.append(l)
        ll = tmp
        if len(ll) == 1:
            break

    print(ll)

    # c02
    for p in range(0, w):
        c0, c1 = 0, 0
        mark = -1
        for l in dd:
            c0 += l[p] == "0"
            c1 += l[p] == "1"
        if c0 <= c1:
            mark = "0"
        else:
            mark = "1"
        tmp = []
        for l in dd:
            if l[p] == mark:
                tmp.append(l)
        dd = tmp
        if len(dd) == 1:
            break

    print(dd)

    on, cn = int(ll[0], 2), int(dd[0], 2)
    return on * cn


if __name__ == "__main__":
    ans = solve2("inp.txt")
    print(ans)

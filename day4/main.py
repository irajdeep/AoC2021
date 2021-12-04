def solve1(path) -> int:
    with open(path) as file:
        ll = file.readlines()
        ll = [l.rstrip() for l in ll]

    ll = [l.rstrip() for l in ll]

    nums = [int(l) for l in ll[0].split(",")]

    boards, tmp, curr = [], [], []

    for l in ll[2:]:
        if len(l) != 0:
            tt = l.split(" ")
            for nn in tt:
                if nn != "":
                    tmp.append(nn)
            curr.append(tmp)
            tmp = []
        else:
            boards.append(curr)
            curr = []

    boards.append(curr)
    mark = {}
    rcount = [[0] * 5 for _ in range(len(boards))]
    ccount = [[0] * 5 for _ in range(len(boards))]
    last = {}
    bb = -1
    curr = -1

    for n in nums:
        curr += 1
        if len(last) == len(boards):
            break
        for b in range(0, len(boards)):
            if len(last) == len(boards):
                break
            for r in range(0, 5):
                if len(last) == len(boards):
                    break
                for c in range(0, 5):
                    if int(boards[b][r][c]) == n:
                        mark[(b, r, c)] = 1
                        rcount[b][r] += 1
                        ccount[b][c] += 1
                        if rcount[b][r] == 5 or ccount[b][c] == 5:
                            mul = n
                            bb = b
                            if b not in last:
                                last[b] = curr

                    if len(last) == len(boards):
                        break

    sums = 0
    for r in range(5):
        for c in range(5):
            if (bb, r, c) not in mark:
                sums += int(boards[bb][r][c])

    print(sums, mul)
    return sums * mul

    print(mark)


if __name__ == "__main__":
    ans = solve1("inp.txt")
    print(ans)

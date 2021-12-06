def solve1(path) -> int:
    lines = open("inp.txt").read().splitlines()

    ll = lines[0].split(",")
    arr = [int(x) for x in ll]

    count = [0] * 9
    for a in arr:
        count[a] += 1

    curr = 0
    for n in range(0, 256):
        curr = count[0]
        for nn in range(0, 8):
            count[nn] = count[nn + 1]
        count[6] += curr
        count[8] = curr

    ans = 0
    for n in count:
        ans += n
    return ans


if __name__ == "__main__":
    ans = solve1("inp.txt")
    print(ans)

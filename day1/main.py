def solve2(path) -> int:
    with open(path) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]

    tmp = []
    for i in range(0, len(lines)):
        x = lines[i]
        if i + 2 < len(lines):
            for j in range(1, 3):
                x += lines[j + i]
            tmp.append(x)

    ans = 0
    for n in range(1, len(tmp)):
        if tmp[n] > tmp[n - 1]:
            ans += 1
    return ans


if __name__ == "__main__":
    ans = solve2("inp.txt")
    print(ans)

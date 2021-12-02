def solve2(path) -> int:
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    h, v, a = 0, 0, 0

    for l in lines:
        nn = l.split(" ")
        dir, dis = nn[0], int(nn[1])

        if dir == "forward":
            h += dis
            v += a * dis
        elif dir == "down":
            a += dis
        else:
            a -= dis

    return h * v


if __name__ == "__main__":
    ans = solve2("inp.txt")
    print(ans)

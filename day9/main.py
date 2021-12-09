def poss(r, c, arr, R, C) -> bool:
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for n in range(4):
        nr = r + dr[n]
        nc = c + dc[n]

        if nr >= 0 and nr < R and nc >= 0 and nc < C:
            if arr[nr][nc] <= arr[r][c]:
                return False
    return True


def bsize(r, c, arr, R, C, vis) -> int:
    # print("here: ", r, c)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    vis[r][c] = True

    ans = 1

    for n in range(4):
        nr = r + dr[n]
        nc = c + dc[n]

        if nr >= 0 and nr < R and nc >= 0 and nc < C:
            if arr[nr][nc] > arr[r][c] and arr[nr][nc] != 9 and not vis[nr][nc]:
                ans = ans + bsize(nr, nc, arr, R, C, vis)

    return ans


def solve2(path) -> int:
    lines = open("inp.txt").read().splitlines()

    arr = []
    for l in lines:
        curr = []
        for ch in l:
            curr.append(int(ch))
        arr.append(curr)

    tmp = []
    vis = [[False] * len(arr[0]) for _ in range(len(arr))]

    for r in range(0, len(arr)):
        for c in range(0, len(arr[0])):
            if poss(r, c, arr, len(arr), len(arr[0])) and not vis[r][c]:
                x = bsize(r, c, arr, len(arr), len(arr[0]), vis)
                # print(r, c, x)
                tmp.append(x)

    tt = sorted(tmp, reverse=True)
    return tt[0] * tt[1] * tt[2]


if __name__ == "__main__":
    ans = solve2("inp.tx")
    print(ans)

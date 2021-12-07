import statistics
import sys


def summ(n):
    return int((n * (n + 1)) / 2)


def solve1(path) -> int:
    lines = open("inp.txt").read().splitlines()
    arr = [int(x) for x in lines[0].split(",")]

    point = int(statistics.median(arr))
    ans = 0

    for nn in arr:
        ans += abs(nn - point)
    return ans


def solve2(path) -> int:
    lines = open("inp.txt").read().splitlines()
    arr = [int(x) for x in lines[0].split(",")]

    mini, maxi = min(arr), max(arr)
    ans = sys.maxsize

    for point in range(mini, maxi + 1):
        dist = 0
        for n in arr:
            dist += summ(abs(point - n))
        ans = min(ans, dist)

    return ans


if __name__ == "__main__":
    ans = solve2("inp.tx")
    print(ans)

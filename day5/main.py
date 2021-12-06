def sign(x):
    return (x > 0) - (x < 0)


def count_overlap(line_segments):
    coordinate_frequencies = {}
    for (x1, y1), (x2, y2) in line_segments:
        if x1 == x2 or y1 == y2 or True:
            x_inc, y_inc = sign(x2 - x1), sign(y2 - y1)
            while (x1, y1) != (x2 + x_inc, y2 + y_inc):
                coordinate_frequencies[(x1, y1)] = (
                    coordinate_frequencies.get((x1, y1), 0) + 1
                )
                x1 += x_inc
                y1 += y_inc
    return sum(frequency > 1 for frequency in coordinate_frequencies.values())


def solve1(path) -> int:
    lines = open("inp.txt").read().splitlines()

    line_segments = []

    for line in lines:
        point1, point2 = line.split(" -> ")
        x1, y1 = map(int, point1.split(","))
        x2, y2 = map(int, point2.split(","))
        line_segments.append(((x1, y1), (x2, y2)))

    return count_overlap(line_segments)


if __name__ == "__main__":
    ans = solve1("inp.txt")
    print(ans)

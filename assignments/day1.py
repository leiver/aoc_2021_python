from tools import timing
import os
import sys


def day1():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day1.txt"), "r")

    prev_depth = 0
    count = 0
    for line in file:
        if int(line) > prev_depth != 0:
            count += 1
        prev_depth = int(line)

    print(count)


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day1.txt"), "r")

    sliding_windows = []
    line_count = 0
    for line in file:
        depth = int(line)
        sliding_windows.append(depth)
        for i in range(1, 3):
            if (line_count - i) >= 0:
                sliding_windows[line_count - i] += depth
        line_count += 1

    prev_depth = 0
    count = 0
    for index in range(len(sliding_windows) - 2):
        if sliding_windows[index] > prev_depth != 0:
            count += 1
        prev_depth = sliding_windows[index]

    print(count)


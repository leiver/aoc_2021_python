from tools import timing
import os
import sys
from more_itertools import pairwise
from more_itertools import sliding_window


def day1():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day1.txt"), "r")

    count = 0
    for prev, next in pairwise(file):
        if int(next) > int(prev):
            count += 1

    print(count)


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day1.txt"), "r")

    count = 0
    for prev_window, next_window in pairwise(sliding_window(map(int, file), 3)):
        if sum(list(next_window)) > sum(list(prev_window)):
            count += 1

    print(count)


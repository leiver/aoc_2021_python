from timing import timing
import os
import sys
from more_itertools import pairwise
from more_itertools import sliding_window


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day1.txt"), "r")

    print(sum(map(lambda pair: 1 if pair[0] < pair[1] else 0, pairwise(map(int, file)))))


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day1.txt"), "r")

    print(sum(map(lambda pair: 1 if pair[0] < pair[1] else 0, pairwise(map(sum, sliding_window(map(int, file), 3))))))


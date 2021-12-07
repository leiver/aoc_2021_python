from timing import timing
import os
import sys
from statistics import median
from statistics import mean
from functools import reduce


def both_parts():
    file = open(os.path.join(sys.path[0], "inputs/input_day7.txt"), "r")

    positions = [int(n) for n in file.readline().split(",")]
    median_pos = int(median(positions))

    print(reduce(lambda acc, pos: acc + abs(pos - median_pos), positions, 0))

    timing.log("Part 1 finished!")

    print(find_sum_distances_increasing(positions, int(mean(positions))))


def find_sum_distances_increasing(positions, point):
    return sum([int(distance*(distance+1)/2) for distance in [abs(position - point) for position in positions]])


def part1():
    both_parts()


def part2():
    both_parts()

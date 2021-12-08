from timing import timing
import os
import sys
from statistics import median
from statistics import mean
from functools import reduce

calculated_sums = {}


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    positions = get_positions_from_file()

    median_pos = int(median(positions))
    print(reduce(lambda acc, pos: acc + abs(pos - median_pos), positions, 0))


def part2():
    positions = get_positions_from_file()

    mean_pos_low = int(mean(positions) - 0.5)
    mean_pos_high = mean_pos_low + 1

    print(min(find_sum_distances_increasing(positions, mean_pos_low), find_sum_distances_increasing(positions, mean_pos_high)))


def find_sum_distances_increasing(positions, point):
    if point not in calculated_sums:
        calculated_sums[point] = sum([int(distance*(distance+1)/2) for distance in [abs(position - point) for position in positions]])
    return calculated_sums[point]


def get_positions_from_file():
    file = open(os.path.join(sys.path[0], "inputs/input_day7.txt"), "r")
    positions = [int(n) for n in file.readline().split(",")]
    return positions

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

    # start looking for the optimal position from the mean of the input data
    current_pos = int(mean(positions))
    prev_pos = current_pos
    step = 1
    # starts by looking left of the mean
    direction = -1
    while True:
        current_sum = find_sum_distances_increasing(positions, current_pos)
        if not is_neighbor_less_than_current(current_pos, current_sum, direction, positions):
            if not is_neighbor_less_than_current(current_pos, current_sum, direction * -1, positions):
                # both neighbors are larger than the current sum, so we are at the optimal position
                result = current_sum
                break
            elif step > 1:
                # in this case we have passed the optimal position
                # we need to do a binary search from the last searched position to the current position to find the actual optimal position
                result = binary_search_sums(positions, range(min(current_pos, prev_pos), max(current_pos, prev_pos) + 1))
                break
            else:
                # in this case the right side is less then the current sum and we are still at the mean position (step == 1)
                # flip the starting direction to traverse right
                direction = 1

        prev_pos = current_pos
        current_pos += step * direction
        # step doubles each time so we expand how much we search at a time for each iteration.
        step *= 2

    print(result)


def is_neighbor_less_than_current(current_pos, current_sum, direction, positions):
    return 0 <= (current_pos + direction) < len(positions) and find_sum_distances_increasing(positions, current_pos + direction) < current_sum


def binary_search_sums(all_positions, search_space):
    median_index = int(len(search_space) / 2)
    while True:
        current_pos_sum = find_sum_distances_increasing(all_positions, search_space[median_index])
        if (median_index-1) >= 0 and find_sum_distances_increasing(all_positions, search_space[median_index-1]) <= current_pos_sum:
            search_space = search_space[:median_index]
        elif (median_index+1) < len(search_space) and find_sum_distances_increasing(all_positions, search_space[median_index+1]) <= current_pos_sum:
            search_space = search_space[median_index:]
        else:
            return current_pos_sum

        median_index = int(len(search_space) / 2)


def find_sum_distances_increasing(positions, point):
    if point not in calculated_sums:
        calculated_sums[point] = sum([int(distance*(distance+1)/2) for distance in [abs(position - point) for position in positions]])
    return calculated_sums[point]


def get_positions_from_file():
    file = open(os.path.join(sys.path[0], "inputs/input_day7.txt"), "r")
    positions = [int(n) for n in file.readline().split(",")]
    return positions

from timing import timing
import os
import sys
from statistics import median


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day7.txt"), "r")

    positions = list(map(int, file.readline().split(",")))
    median_pos = int(median(positions))
    solution = 0
    for position in positions:
        solution += abs(position - median_pos)

    print(solution)


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day7.txt"), "r")


    initial_positions = sorted(list(map(int, file.readline().split(","))))
    positions = range(min(initial_positions), max(initial_positions)+1)
    median_index = int(len(positions) / 2)
    while True:
        current_pos_sum = find_sum_distances_increasing(initial_positions, positions[median_index])
        if len(positions) == 1:
            print(current_pos_sum)
            break
        if (median_index-1) >= 0 and find_sum_distances_increasing(initial_positions, positions[median_index-1]) <= current_pos_sum:
            direction_left = True
        elif (median_index+1) < len(positions) and find_sum_distances_increasing(initial_positions, positions[median_index+1]) <= current_pos_sum:
            direction_left = False
        else:
            print(current_pos_sum)
            break

        if direction_left:
            positions = positions[:median_index]
        else:
            positions = positions[median_index:]
        median_index = int(len(positions) / 2)



def find_sum_distances_increasing(positions, point):
    solution = 0
    for position in positions:
        solution += sum(range(abs(position - point)+1))
    return solution

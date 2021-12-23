from timing import timing
import os
import sys
from itertools import combinations


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day22.txt"), "r")

    active_cubes = set()

    for line in file:
        action, coords = line.strip().split(" ")
        x_ranges, y_ranges, z_ranges = [tuple(map(int, coord[2:].split(".."))) for coord in coords.split(",")]
        if in_bounds(x_ranges) and in_bounds(y_ranges) and in_bounds(z_ranges):
            for x in range(x_ranges[0], x_ranges[1] + 1):
                for y in range(y_ranges[0], y_ranges[1] + 1):
                    for z in range(z_ranges[0], z_ranges[1] + 1):
                        if action == "on":
                            active_cubes.add((x, y, z))
                        else:
                            active_cubes.discard((x, y, z))

    print(len(active_cubes))


def in_bounds(coord_range):
    return -50 <= coord_range[0] and 50 >= coord_range[1]


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day22.txt"), "r")

    active_cubes = set()

    actions = []
    for line in file:
        action, coords = line.strip().split(" ")
        x_ranges, y_ranges, z_ranges = [tuple(map(int, coord[2:].split(".."))) for coord in coords.split(",")]
        actions.append((action, x_ranges, y_ranges, z_ranges))

    for step, action, x_ranges, y_ranges, z_ranges in enumerate(actions):
        if action == "on":
            action_combinations = [
                (number_of_combinations, combinations(actions[step+1:], number_of_combinations))
                for number_of_combinations
                in range(1, len(actions) - step - 1)
            ]

            cubes_to_remove_from_current_action = [
                sum(
                    max(max([x_ranges[1]] + [x[1] for _, x, _, _ in combination]) - min([x_ranges[0]] + [x[0] for _, x, _, _ in combination]), 0) *
                    max(max([y_ranges[1]] + [y[1] for _, _, y, _ in combination]) - min([y_ranges[0]] + [y[0] for _, _, y, _ in combination]), 0) *
                    max(max([z_ranges[1]] + [z[1] for _, _, _, z in combination]) - min([z_ranges[0]] + [z[0] for _, _, _, z in combination]), 0)
                ) * (1 if number_of_combinations % 2 else -1)
                for number_of_combinations, combination
                in action_combinations
            ]

    print(len(active_cubes))


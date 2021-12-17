import math

from timing import timing
import os
import sys
from itertools import product as list_product


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day17.txt"), "r")

    x_range, y_range = file.read().strip()[15:].split(", y=")
    y_min, y_max = y_range.split("..")

    y_velocity = (int(y_min) * -1) - 1

    highest_y = int((y_velocity * (y_velocity + 1)) / 2)

    print(highest_y)


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day17.txt"), "r")

    x_range, y_range = file.read().strip()[15:].split(", y=")
    x_min, x_max = tuple(map(int, x_range.split("..")))
    y_min, y_max = tuple(map(int, y_range.split("..")))

    max_steps_y = (((y_min * -1) - 1) * 2) + 1
    max_y_velocity = (y_min * -1) - 1
    max_steps_x = int(math.sqrt(x_min * 2))
    while ((max_steps_x + 1) * (max_steps_x + 2)) / 2 <= x_max:
        max_steps_x += 1

    unique_velocity_combinations = set()
    for step in range(1, max_steps_y + 2):

        valid_x_velocities_for_step = []
        for x_velocity in range(max_steps_x, x_max + 1):
            x_after_steps = sum(range(max(1, x_velocity - step + 1), x_velocity + 1))
            if x_min <= x_after_steps <= x_max:
                valid_x_velocities_for_step.append(x_velocity)
            elif x_after_steps > x_max:
                break

        valid_y_velocities_for_step = []
        for y_velocity in range(y_min, max_y_velocity + 1):
            y_after_steps = sum(range(y_velocity - step + 1, y_velocity + 1))
            if y_min <= y_after_steps <= y_max:

                valid_y_velocities_for_step.append(y_velocity)
            elif y_after_steps > y_max:
                break

        unique_velocity_combinations_for_step = set(list_product(valid_x_velocities_for_step, valid_y_velocities_for_step))

        unique_velocity_combinations.update(unique_velocity_combinations_for_step)

    print(len(unique_velocity_combinations))

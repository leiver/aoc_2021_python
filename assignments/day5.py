from timing import timing
import os
import sys
import re


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day5.txt"), "r")

    seafloor_map = {}
    for line in file:
        (x1, y1, x2, y2) = map(int, re.split(',| -> ', line.strip()))
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                seafloor_map[(x1, i)] = seafloor_map[(x1, i)] + 1 if (x1, i) in seafloor_map else 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                seafloor_map[(i, y1)] = seafloor_map[(i, y1)] + 1 if (i, y1) in seafloor_map else 1


    print(sum([1 if point > 1 else 0 for point in seafloor_map.values()]))


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day5.txt"), "r")

    seafloor_map = {}
    for line in file:
        (x1, y1, x2, y2) = map(int, re.split(',| -> ', line.strip()))
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                seafloor_map[(x1, i)] = seafloor_map[(x1, i)] + 1 if (x1, i) in seafloor_map else 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                seafloor_map[(i, y1)] = seafloor_map[(i, y1)] + 1 if (i, y1) in seafloor_map else 1
        else:
            step_direction_x = 1 if x1 < x2 else -1
            steps_x = range(x1, x2 + step_direction_x, step_direction_x)
            step_direction_y = 1 if y1 < y2 else -1
            steps_y = range(y1, y2 + step_direction_y, step_direction_y)
            for i in range(len(steps_x)):
                seafloor_map[(steps_x[i], steps_y[i])] = seafloor_map[(steps_x[i], steps_y[i])] + 1 if (steps_x[i], steps_y[i]) in seafloor_map else 1


    print(sum([1 if point > 1 else 0 for point in seafloor_map.values()]))

from timing import timing
import os
import sys
import numpy as np

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def both_parts():
    file = open(os.path.join(sys.path[0], "inputs/input_day11.txt"), "r")

    octopus_map = []
    for line in file:
        octopus_map.append(np.array(list(map(int, line.strip()))))
    octopus_map = np.array(octopus_map)

    total_flashes = 0
    step = 0
    while True:
        if step == 100:
            print(total_flashes)
            timing.log("Part 1 finished!")
        triggered_octopus = set()
        for x in range(len(octopus_map)):
            for y in range(len(octopus_map[x])):
                check_octopus((x, y), octopus_map, triggered_octopus)
        total_flashes += len(triggered_octopus)
        for (x, y) in triggered_octopus:
            octopus_map[x][y] = 0
        step += 1
        if len(triggered_octopus) == (len(octopus_map) * len(octopus_map[0])):
            print(step)
            break


def check_octopus(coords, octopus_map, triggered_octopus):
    (x, y) = coords
    if 0 <= x < len(octopus_map) and 0 <= y < len(octopus_map[0]):
        octopus_map[x][y] += 1
        if octopus_map[x][y] > 9 and coords not in triggered_octopus:
            triggered_octopus.update({coords})
            for direction in directions:
                check_octopus(tuple(np.add(coords, direction)), octopus_map, triggered_octopus)


def part1():
    both_parts()


def part2():

    both_parts()


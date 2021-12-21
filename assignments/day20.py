from timing import timing
import os
import sys
from itertools import permutations
from numpy import add as np_add

directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
opposite_pixel_value = {"#": ".", ".": "#"}


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day20.txt"), "r")

    algorithm, image = file.read().strip().split("\n\n")

    image_map = {}
    for y, line in enumerate(image.split("\n")):
        for x, pixel in enumerate(line.strip()):
            if pixel == "#":
                image_map.update({(x, y): pixel})

    default_pixel = "."
    for _ in range(2):
        parsed_pixels = set()
        new_map = {}
        for pixel_coordinate in image_map:
            for neighbor in [tuple(np_add(direction, pixel_coordinate)) for direction in directions]:
                if neighbor not in parsed_pixels:
                    parsed_pixels.add(neighbor)
                    algorithm_index = int("".join(["1" if image_map.get(tuple(np_add(direction, neighbor)), default_pixel) == "#" else "0" for direction in directions]), 2)
                    if algorithm[algorithm_index] == default_pixel:
                        new_map.update({neighbor: default_pixel})
        image_map = new_map
        default_pixel = opposite_pixel_value[default_pixel]

    print(len(image_map))


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day20.txt"), "r")

    algorithm, image = file.read().strip().split("\n\n")

    image_map = {}
    for y, line in enumerate(image.split("\n")):
        for x, pixel in enumerate(line.strip()):
            if pixel == "#":
                image_map.update({(x, y): pixel})

    default_pixel = "."
    for _ in range(50):
        parsed_pixels = set()
        new_map = {}
        for pixel_coordinate in image_map:
            for neighbor in [tuple(np_add(direction, pixel_coordinate)) for direction in directions]:
                if neighbor not in parsed_pixels:
                    parsed_pixels.add(neighbor)
                    algorithm_index = int("".join(["1" if image_map.get(tuple(np_add(direction, neighbor)), default_pixel) == "#" else "0" for direction in directions]), 2)
                    if algorithm[algorithm_index] == default_pixel:
                        new_map.update({neighbor: default_pixel})
        image_map = new_map
        default_pixel = opposite_pixel_value[default_pixel]

    print(len(image_map))


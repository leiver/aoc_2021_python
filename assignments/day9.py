from timing import timing
import os
import sys
from numpy import add
from numpy import prod

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    cave_map = get_cave_map_from_file()

    print(sum([(1 + value) * int(all([cave_map.get(neighbor, 10) > value for neighbor in [tuple(add(coords, direction)) for direction in directions]])) for coords, value in cave_map.items()]))


def part2():
    cave_map = get_cave_map_from_file()

    basins = []
    coords_to_basins = {}
    for coords, value in cave_map.items():
        if value != 9 and coords not in coords_to_basins:
            basins.append(map_whole_basin(cave_map, coords_to_basins, coords, len(basins)))

    print(prod(list(sorted(map(len, basins), reverse=True))[:3]))


def map_whole_basin(cave_map, coords_to_basin, current_coord, basin_number):
    coords_to_basin.update({current_coord: basin_number})
    basin = [current_coord]
    for neighbor in [tuple(add(current_coord, direction)) for direction in directions]:
        if cave_map.get(neighbor, 9) < 9 and neighbor not in coords_to_basin:
            basin += map_whole_basin(cave_map, coords_to_basin, neighbor, basin_number)
    return basin


def get_cave_map_from_file():
    file = open(os.path.join(sys.path[0], "inputs/input_day9.txt"), "r")
    cave_map = {}
    row = 0
    for line in file:
        cave_map.update({(row, column): int(line[column]) for column in range(len(line.strip()))})
        row += 1
    return cave_map


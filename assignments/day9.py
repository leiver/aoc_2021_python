from timing import timing
import os
import sys
from numpy import add
from numpy import array
from numpy import prod

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    cave_map = get_cave_map_from_file()

    lowest_points = 0
    for coords, value in cave_map.items():
        lower_neighbor_found = False
        for direction in directions:
            neighbor_coords = tuple(add(coords, direction))
            if neighbor_coords in cave_map and cave_map[neighbor_coords] <= value:
                lower_neighbor_found = True
                break
        if not lower_neighbor_found:
            lowest_points += 1 + value

    print(lowest_points)


def part2():
    cave_map = get_cave_map_from_file()

    basins = []
    coords_to_basins = {}
    for coords, value in cave_map.items():
        if value != 9:
            for direction in directions:
                neighbor_coords = tuple(add(coords, direction))
                if neighbor_coords in cave_map and cave_map[neighbor_coords] != 9:
                    if neighbor_coords in coords_to_basins:
                        if coords not in coords_to_basins:
                            basin = coords_to_basins[neighbor_coords]
                            basins[basin].append(coords)
                            coords_to_basins[coords] = basin
                        elif coords_to_basins[neighbor_coords] != coords_to_basins[coords]:
                            basin = coords_to_basins[coords]
                            neighbor_basin = coords_to_basins[neighbor_coords]
                            basins[basin].extend(basins[neighbor_basin])
                            for neighbor_basin_coord in basins[neighbor_basin]:
                                coords_to_basins[neighbor_basin_coord] = basin
                            basins[neighbor_basin] = []
                    elif coords not in coords_to_basins:
                        coords_to_basins[coords] = len(basins)
                        basins.append([coords])

    print(prod(list(sorted(map(len, basins), reverse=True))[:3]))


def get_cave_map_from_file():
    file = open(os.path.join(sys.path[0], "inputs/input_day9.txt"), "r")
    cave_map = {}
    row = 0
    for line in file:
        cave_map.update({(row, column): int(line[column]) for column in range(len(line.strip()))})
        row += 1
    return cave_map


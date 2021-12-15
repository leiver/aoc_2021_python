from timing import timing
import os
import sys
from numpy import add
from heapq import heappush
from heapq import heappop

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    risks, max_x, max_y = initialize_risks_from_file()

    lowest_risk, paths = find_shortest_path_a_star(risks, max_x, max_y)

    print(lowest_risk)


def part2():
    risks, initial_max_x, initial_max_y = initialize_risks_from_file()
    initial_max_x = initial_max_x + 1
    initial_max_y = initial_max_y + 1

    for tile_x in range(5):
        for tile_y in range(5):
            if tile_x != 0 or tile_y != 0:
                if tile_x - 1 >= 0:
                    neighbor_x = tile_x - 1
                    neighbor_y = tile_y
                else:
                    neighbor_y = tile_y - 1
                    neighbor_x = tile_x

                for x in range(initial_max_x):
                    for y in range(initial_max_y):
                        risks[(x + (initial_max_x * tile_x), y + (initial_max_y * tile_y))] = \
                            (risks[(x + (initial_max_x * neighbor_x), y + (initial_max_y * neighbor_y))] % 9) + 1

    new_max_x = (initial_max_x * 5) - 1
    new_max_y = (initial_max_y * 5) - 1
    lowest_risk, paths = find_shortest_path_a_star(risks, new_max_x, new_max_y)

    print(lowest_risk)


def initialize_risks_from_file():
    file = open(os.path.join(sys.path[0], "inputs/input_day15.txt"), "r")

    risks = {}
    max_x = 0
    max_y = 0
    for y, line in enumerate(file):
        for x, node in enumerate(line.strip()):
            risks[(x, y)] = int(node)
            max_y = max(max_y, y)
            max_x = max(max_x, x)
    return risks, max_x, max_y


def find_shortest_path_a_star(risks, max_x, max_y):
    end = (max_x, max_y)
    heap = []
    heappush(heap, (max_x + max_y, ((0, 0), (-1, -1))))
    parsed_paths = {}
    added_to_queue = {(0, 0): max_x + max_y}
    while heap:
        cost_so_far, (current_coord, past_coord) = heappop(heap)
        risk_so_far = cost_so_far - min_risk_between_two_points(current_coord, end)
        if current_coord not in parsed_paths:
            parsed_paths[current_coord] = past_coord
            if current_coord == end:
                return risk_so_far, parsed_paths
            for neighbor in [tuple(add(direction, current_coord)) for direction in directions]:
                if neighbor in risks:
                    cost_for_neighbor = risk_so_far + risks[neighbor] + min_risk_between_two_points(neighbor, end)
                    if neighbor not in added_to_queue or added_to_queue[neighbor] > cost_for_neighbor:
                        added_to_queue[neighbor] = cost_for_neighbor
                        heappush(heap, (cost_for_neighbor, (neighbor, current_coord)))


def min_risk_between_two_points(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return abs(a_x - b_x) + abs(a_y - b_y)


def print_path(current_coord, parsed_paths):
    while True:
        print(current_coord, end='')
        if current_coord in parsed_paths:
            current_coord = parsed_paths[current_coord]
            print(" -> ", end='')
        else:
            print()
            break


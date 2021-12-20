import math

from timing import timing
import os
import sys
from itertools import combinations
from itertools import product as list_product
from numpy import array as np_array
from numpy import full as np_full


def both_parts():
    file = open(os.path.join(sys.path[0], "inputs/input_day19.txt"), "r")

    beacons_in_scanner_range = {}
    for scanner_lines in file.read().strip().split("\n\n"):
        scanner_lines = scanner_lines.split("\n")
        scanner_id = scanner_lines[0].strip().strip("--- scanner ").strip(" ---")
        beacons_in_scanner_range.update({scanner_id: [tuple(map(int, beacon.strip().split(","))) for beacon in scanner_lines[1:]]})

    beacon_distances_for_scanners = {}
    for scanner_id, beacons in beacons_in_scanner_range.items():
        distances = []
        for beacon_comination in combinations(enumerate(beacons), 2):
            first_beacon, second_beacon = beacon_comination
            first_beacon_id, first_beacon_coordinates = first_beacon
            second_beacon_id, second_beacon_coordinates = second_beacon
            distances.append((
                (first_beacon_id, second_beacon_id),
                [
                    first_vector - second_vector
                    for first_vector, second_vector
                    in zip(first_beacon_coordinates, second_beacon_coordinates)
                ]
            ))
        beacon_distances_for_scanners.update({scanner_id: distances})

    parsed_scanners = {"0": (0, 0, 0)}
    scanner_queue = [("0", {0: 0, 1: 1, 2: 2}, [1, 1, 1])]
    known_beacons = set(beacons_in_scanner_range["0"])
    while scanner_queue:
        current_scanner, current_swap, current_signs = scanner_queue.pop()
        current_scanner_beacon_distances = beacon_distances_for_scanners[current_scanner]
        for scanner_to_parse in beacon_distances_for_scanners.keys() - parsed_scanners.keys():
            distances_to_parse = beacon_distances_for_scanners[scanner_to_parse]
            matched_distances = list(filter(
                lambda distance_combination: sorted(map(abs, distance_combination[0][1])) == sorted(map(abs, distance_combination[1][1])),
                list_product(current_scanner_beacon_distances, distances_to_parse)
            ))
            if len(matched_distances) >= int((11*12)/2):
                current_scanner_beacons, current_scanner_beacon_distance = matched_distances[0][0]
                parsing_scanner_beacons, parsing_scanner_beacon_distance = matched_distances[0][1]

                parsing_scanner_beacon = parsing_scanner_beacons[0]
                if parsing_scanner_beacons[1] == matched_distances[1][1][0][0] or parsing_scanner_beacons[1] == matched_distances[1][1][0][1]:
                    parsing_scanner_beacon_distance = tuple(np_array(parsing_scanner_beacon_distance) * np_array([-1, -1, -1]))
                    parsing_scanner_beacon = parsing_scanner_beacons[1]
                swaps = {}
                signs = []
                for i in range(3):
                    for j in range(3):
                        if (abs(current_scanner_beacon_distance[current_swap[i]] * current_signs[i])) == abs(parsing_scanner_beacon_distance[(i+j) % 3]):
                            swaps.update({i: (i + j) % 3})
                            break
                    signs.append(int((current_scanner_beacon_distance[current_swap[i]] * current_signs[i]) / parsing_scanner_beacon_distance[swaps[i]]))

                beacons_in_scanner_range[scanner_to_parse] = [
                    tuple([beacon[swaps[i]] * signs[i] for i, beacon_coordinate in enumerate(beacon)])
                    for beacon
                    in beacons_in_scanner_range[scanner_to_parse]
                ]

                distance_from_parsing_to_zero = np_array(beacons_in_scanner_range[current_scanner][current_scanner_beacons[0]]) - np_array(beacons_in_scanner_range[scanner_to_parse][parsing_scanner_beacon])
                beacons_in_scanner_range[scanner_to_parse] = [
                    tuple(np_array(beacon) + distance_from_parsing_to_zero)
                    for beacon
                    in beacons_in_scanner_range[scanner_to_parse]
                ]

                known_beacons.update(set(beacons_in_scanner_range[scanner_to_parse]))
                scanner_queue.append((scanner_to_parse, swaps, signs))
                parsed_scanners.update({scanner_to_parse: tuple(distance_from_parsing_to_zero)})

    print(len(known_beacons))

    timing.log("Part 1 finished!")

    max_distance = 0
    for first_scanner, second_scanner in combinations(parsed_scanners.values(), 2):
        manhatten_distance = abs(first_scanner[0] - second_scanner[0]) + abs(first_scanner[1] - second_scanner[1]) + abs(first_scanner[2] - second_scanner[2])
        max_distance = max(max_distance, manhatten_distance)

    print(max_distance)


def part1():
    both_parts()


def part2():
    both_parts()

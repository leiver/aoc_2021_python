import math

from timing import timing
import os
import sys
from itertools import combinations
from itertools import product as list_product
from numpy import array as np_array
from numpy import full as np_full


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/tests/input_day19_test.txt"), "r")

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

    parsed_scanners = {"0"}
    scanner_queue = [("0", {0: 0, 1: 1, 2: 2}, [1, 1, 1])]
    known_beacons = set(beacons_in_scanner_range["0"])
    while scanner_queue:
        current_scanner, current_swap, current_signs = scanner_queue.pop()
        #print(current_scanner, current_swap, current_signs)
        current_scanner_beacon_distances = beacon_distances_for_scanners[current_scanner]
        for scanner_to_parse in beacon_distances_for_scanners.keys() - parsed_scanners:
            distances_to_parse = beacon_distances_for_scanners[scanner_to_parse]
            matched_distances = list(filter(
                lambda distance_combination: sorted(map(abs, distance_combination[0][1])) == sorted(map(abs, distance_combination[1][1])),
                list_product(current_scanner_beacon_distances, distances_to_parse)
            ))
            if len(matched_distances) >= int((11*12)/2):
                current_scanner_beacons, current_scanner_beacon_distance = matched_distances[0][0]
                parsing_scanner_beacons, parsing_scanner_beacon_distance = matched_distances[0][1]

                #print(matched_distances[0], matched_distances[1])
                #print(f"{parsing_scanner_beacons[1]} == {matched_distances[1][1][0][0]}")
                if parsing_scanner_beacons[1] == matched_distances[1][1][0][0] or parsing_scanner_beacons[1] == matched_distances[1][1][0][1]:
                    parsing_scanner_beacon_distance = tuple(np_array(parsing_scanner_beacon_distance) * np_array([-1, -1, -1]))
                swaps = {}
                signs = []
                #print(current_scanner_beacon_distance)
                #print(parsing_scanner_beacon_distance)
                for i in range(3):
                    for j in range(3):
                        #print(f"{current_scanner_beacon_distance[current_swap[i]] * current_signs[i]} == {parsing_scanner_beacon_distance[(i+j) % 3]}")
                        if (abs(current_scanner_beacon_distance[current_swap[i]] * current_signs[i])) == abs(parsing_scanner_beacon_distance[(i+j) % 3]):
                            swaps.update({i: (i + j) % 3})
                            break
                    #print(f"{current_scanner_beacon_distance[current_swap[i]] * current_signs[i]} / {parsing_scanner_beacon_distance[swaps[i]]} = {int((current_scanner_beacon_distance[current_swap[i]] * current_signs[i]) / parsing_scanner_beacon_distance[swaps[i]])}")
                    signs.append(int((current_scanner_beacon_distance[current_swap[i]] * current_signs[i]) / parsing_scanner_beacon_distance[swaps[i]]))

                #print(swaps, signs)
                #for beacon in beacons_in_scanner_range[scanner_to_parse]:
                #    print(beacon)
                #print()
                beacons_in_scanner_range[scanner_to_parse] = [
                    tuple([beacon[swaps[i]] * signs[i] for i, beacon_coordinate in enumerate(beacon)])
                    for beacon
                    in beacons_in_scanner_range[scanner_to_parse]
                ]

                #for beacon in beacons_in_scanner_range[scanner_to_parse]:
                #    print(beacon)
                #print()

                #distance_from_parsing_to_current = int(math.sqrt(
                #    math.pow(math.sqrt(sum([math.pow(beacon_coord, 2) for beacon_coord in beacons_in_scanner_range[current_scanner][current_scanner_beacons[0]]])), 2) +
                #    math.pow(math.sqrt(sum([math.pow(beacon_coord, 2) for beacon_coord in beacons_in_scanner_range[scanner_to_parse][parsing_scanner_beacons[0]]])), 2)
                #))
                #print(distance_from_parsing_to_current)
                #print(beacons_in_scanner_range[current_scanner][current_scanner_beacons[0]])
                #print(beacons_in_scanner_range[scanner_to_parse][parsing_scanner_beacons[0]])

                distance_from_parsing_to_zero = np_array(beacons_in_scanner_range[current_scanner][current_scanner_beacons[0]]) - np_array(beacons_in_scanner_range[scanner_to_parse][parsing_scanner_beacons[0]])
                #print(f"{beacons_in_scanner_range[current_scanner][current_scanner_beacons[0]]} - {beacons_in_scanner_range[scanner_to_parse][parsing_scanner_beacons[0]]} = {distance_from_parsing_to_zero}")
                beacons_in_scanner_range[scanner_to_parse] = [
                    tuple(np_array(beacon) + distance_from_parsing_to_zero)
                    for beacon
                    in beacons_in_scanner_range[scanner_to_parse]
                ]

                known_beacons.update(set(beacons_in_scanner_range[scanner_to_parse]))
                scanner_queue.append((scanner_to_parse, swaps, signs))
                parsed_scanners.add(scanner_to_parse)
                #print(f"done with scanner {scanner_to_parse} connected to {current_scanner}")

                #for matched_distance in matched_distances:
                    #print(matched_distance)
                #beacon_in_current = beacons_in_scanner_range[current_scanner][matched_distances[0][0][0][0]]
                #beacons_in_current = [beacons_in_scanner_range[current_scanner][beacon] for beacon in matched_distances[0][0][0]]
                #sorted_abs_coords_in_current = sorted(map(abs, beacon_in_current))
                #beacons_in_parsed = [beacons_in_scanner_range[scanner_to_parse][beacon] for beacon in matched_distances[0][1][0]]
                #print(beacon_in_current)
                #print(beacons_in_current)
                #print(beacons_in_parsed)
                #beacon_in_parsed = list(filter(lambda beacon: sorted_abs_coords_in_current == sorted(map(abs, beacon)), beacons_in_parsed))[0]
                #print(beacon_in_parsed)

    file = open(os.path.join(sys.path[0], "inputs/tests/input_day19_test_result.txt"), "r")
    for beacon, result in zip(sorted(known_beacons), sorted([tuple(map(int, line.strip().split(","))) for line in file.readlines()])):
        if beacon != result:
            print(f"{beacon[0]},{beacon[1]},{beacon[2]}")
    print(len(known_beacons))
    #for first_scanner_distances, second_scanner_distances in combinations(beacon_distances_for_scanners.items(), 2):
        #first_scanner_id, first_scanner_distances = first_scanner_distances
        #second_scanner_id, second_scanner_distances = second_scanner_distances
        #print(first_scanner_distances)
        #print()
        #print(second_scanner_distances)
        #matched_distances = list(filter(lambda distance_combination: distance_combination[0][1] == distance_combination[1][1], list_product(first_scanner_distances, second_scanner_distances)))
        #print(matched_distances)
        #print(len(matched_distances), int((11*12)/2))
        #matched_beacons_for_first_scanner = {beacon for beacon_pair in [matched_distance[0][0] for matched_distance in matched_distances] for beacon in beacon_pair}
        #for beacon in matched_beacons_for_first_scanner:
            #print(",".join(list(map(str, beacons_in_scanner_range[first_scanner_id][beacon]))))
        #print([beacons_in_scanner_range[first_scanner_id][beacon] for beacon in matched_beacons_for_first_scanner])
        #print()
        #matched_beacons_for_second_scanner = {beacon for beacon_pair in [matched_distance[1][0] for matched_distance in matched_distances] for beacon in beacon_pair}
        #for beacon in matched_beacons_for_second_scanner:
            #print(",".join(list(map(str, beacons_in_scanner_range[second_scanner_id][beacon]))))
        #print([beacons_in_scanner_range[second_scanner_id][beacon] for beacon in matched_beacons_for_second_scanner])



def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day19.txt"), "r")

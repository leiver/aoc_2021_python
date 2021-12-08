from timing import timing
import os
import sys
from functools import reduce


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day8.txt"), "r")

    count = 0
    for line in file:
        (patterns, output) = line.strip().split(" | ")
        for pattern in output.split(" "):
            if len(pattern) in [2, 3, 4, 7]:
                count += 1

    print(count)



def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day8.txt"), "r")

    print(sum([sum_output_for_segment(line) for line in file]))


def sum_output_for_segment(line):
    (patterns, output) = [entry.split(" ") for entry in line.strip().split(" | ")]
    pattern_map = reduce(lambda acc, entry: dict(acc, **{str(len(entry)): acc[str(len(entry))] + [sorted(list(entry))] if str(len(entry)) in acc else [sorted(list(entry))]}), patterns, {})
    number_map = {}
    number_map[1] = pattern_map["2"][0]
    number_map[7] = pattern_map["3"][0]
    number_map[4] = pattern_map["4"][0]
    number_map[8] = pattern_map["7"][0]
    segment_map = {"top right": number_map[1], "bottom right": number_map[1]}
    segment_map["top"] = list(filter(lambda wire: wire not in number_map[1], number_map[7]))
    mid_top_left = list(filter(lambda wire: wire not in number_map[7], number_map[4]))
    segment_map["mid"] = mid_top_left
    segment_map["top left"] = mid_top_left
    rest = list(filter(lambda wire: wire not in number_map[4], number_map[8]))
    segment_map["bottom left"] = rest
    segment_map["bottom"] = rest

    number_map[3] = list(filter(lambda number: all(wire in number for wire in number_map[1]), pattern_map["5"]))[0]
    segment_map["bottom"] = list(filter(lambda wire: wire in number_map[3], segment_map["bottom"]))
    segment_map["bottom left"] = list(filter(lambda wire: wire not in number_map[3], segment_map["bottom left"]))
    segment_map["mid"] = list(filter(lambda wire: wire in number_map[3], segment_map["mid"]))
    segment_map["top left"] = list(filter(lambda wire: wire not in number_map[3], segment_map["top left"]))

    number_map[2] = list(filter(lambda number: all(wire in number for wire in segment_map["bottom left"]), pattern_map["5"]))[0]
    segment_map["top right"] = list(filter(lambda wire: wire in number_map[2], segment_map["top right"]))
    segment_map["bottom right"] = list(filter(lambda wire: wire not in number_map[2], segment_map["bottom right"]))

    number_map[5] = list(filter(lambda number: all(wire in number for wire in segment_map["top left"]), pattern_map["5"]))[0]
    number_map[6] = list(filter(lambda number: all(wire not in number for wire in segment_map["top right"]), pattern_map["6"]))[0]
    number_map[9] = list(filter(lambda number: all(wire not in number for wire in segment_map["bottom left"]), pattern_map["6"]))[0]

    print(number_map)
    return map_output_to_number(number_map, output)


def map_output_to_number(number_map, output):
    result = ""
    for pattern in output:
        pattern = sorted(list(pattern))
        print(pattern)
        if len(pattern) == 2:
            result += "1"
        elif len(pattern) == 3:
            result += "7"
        elif len(pattern) == 4:
            result += "4"
        elif len(pattern) == 7:
            result += "8"
        elif len(pattern) == 5:
            if pattern == number_map[3]:
                result += "3"
            elif pattern == number_map[2]:
                result += "2"
            elif pattern == number_map[5]:
                result += "5"
        elif len(pattern) == 6:
            if pattern == number_map[6]:
                result += "6"
            elif pattern == number_map[9]:
                result += "9"
            else:
                result += "0"

    print(result)
    return int(result)

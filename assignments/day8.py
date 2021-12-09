import string

from timing import timing
import os
import sys

segment_mapping = {"top": 0, "top left": 1, "top right": 2, "mid": 3, "bottom left": 4, "bottom right": 5, "bottom": 6}


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

    print(sum([find_number_for_entry(line) for line in file]))


def find_number_for_entry(line):

    (patterns, output) = [entry.split(" ") for entry in line.strip().split(" | ")]

    wire_map = create_wire_map(patterns)

    return int(make_number_from_output(output, wire_map))


def make_number_from_output(output, wire_map):
    result = ""
    for output_pattern in [set(pattern) for pattern in output]:
        if len(output_pattern) == 2:
            result += "1"
        elif len(output_pattern) == 3:
            result += "7"
        elif len(output_pattern) == 4:
            result += "4"
        elif len(output_pattern) == 7:
            result += "8"
        else:
            filtered_wire_map = [wires & output_pattern for wires in wire_map]
            if len(filtered_wire_map[segment_mapping["mid"]]) == 1 and len(filtered_wire_map[segment_mapping["top right"]]) == 1:
                result += "2"
            elif len(filtered_wire_map[segment_mapping["mid"]]) == 1 and len(filtered_wire_map[segment_mapping["bottom"]]) == 1:
                result += "3"
            elif len(filtered_wire_map[segment_mapping["bottom"]]) == 1 and len(filtered_wire_map[segment_mapping["top right"]]) == 1:
                result += "5"
            elif len(filtered_wire_map[segment_mapping["mid"]]) == 1:
                result += "0"
            elif len(filtered_wire_map[segment_mapping["top right"]]) == 1:
                result += "6"
            elif len(filtered_wire_map[segment_mapping["bottom"]]) == 1:
                result += "9"
    return result


def create_wire_map(patterns):
    wires = set(string.ascii_lowercase[:7])

    wire_map = [wires for _ in range(7)]
    for pattern in [set(x) for x in patterns]:
        mask = None
        if len(pattern) == 2:
            mask = [segment_mapping["top right"], segment_mapping["bottom right"]]
        elif len(pattern) == 3:
            mask = [segment_mapping["top right"], segment_mapping["bottom right"], segment_mapping["top"]]
        elif len(pattern) == 4:
            mask = [segment_mapping["top right"], segment_mapping["bottom right"], segment_mapping["mid"], segment_mapping["top left"]]
        if mask:
            wire_map = [wire_map[i] & pattern if i in mask else wire_map[i] - pattern for i in range(len(wire_map))]
    return wire_map

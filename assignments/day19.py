from timing import timing
import os
import sys


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day19.txt"), "r")

    for scanner_lines in file.read().strip().split("\n\n"):
        scanner_lines = scanner_lines.split("\n")
        scanner_id = scanner_lines[0]
        print(scanner_id)
        for beacon in scanner_lines[1:]:
            print()


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day19.txt"), "r")

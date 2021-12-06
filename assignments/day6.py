from timing import timing
import os
import sys


def both_parts():
    file = open(os.path.join(sys.path[0], "inputs/input_day6.txt"), "r")

    timers = list(map(int, file.readline().strip().split(",")))

    birth_cycles = [0 for _ in range(9)]

    for timer in timers:
        birth_cycles[timer] += 1

    for day in range(256):
        if day == 80:
            print("part 1: {0}".format(sum(birth_cycles)))

        birth_cycle_index = day % 9
        if birth_cycles[birth_cycle_index] > 0:
            birth_cycles[(birth_cycle_index + 7) % 9] += birth_cycles[birth_cycle_index]

    print("part 2: {0}".format(sum(birth_cycles)))


def part1():
    both_parts()


def part2():
    both_parts()


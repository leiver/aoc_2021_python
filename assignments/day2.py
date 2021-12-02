from timing import timing
import os
import sys
from functools import reduce
from operator import mul


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    print(reduce(mul, reduce(lambda posdep, com: map(lambda pair: pair[0] + (pair[1] * int(com[1])), zip(posdep, {"forward": [1, 0], "up": [0, -1], "down": [0, 1]}[com[0]])), map(lambda line: line.split(" "), open(os.path.join(sys.path[0], "inputs/input_day2.txt"), "r")), [0, 0])))


def part1_initial_solution():
    file = open(os.path.join(sys.path[0], "inputs/input_day2.txt"), "r")

    position = 0
    depth = 0
    for line in file:
        (command, amount) = line.split(" ")
        if command == "forward":
            position += int(amount)
        elif command == "up":
            depth -= int(amount)
        elif command == "down":
            depth += int(amount)

    print(position * depth)


def part2():
    print(reduce(mul, reduce(lambda posdepaim, com: list(map(lambda triple: triple[0] + (triple[1] * triple[2] * int(com[1])), zip(posdepaim, [1, posdepaim[2], 1], {"forward": [1, 1, 0], "up": [0, 0, -1], "down": [0, 0, 1]}[com[0]]))), map(lambda line: line.split(" "), open(os.path.join(sys.path[0], "inputs/input_day2.txt"), "r")), [0, 0, 0])[:-1]))


def part2_initial_solution():
    file = open(os.path.join(sys.path[0], "inputs/input_day2.txt"), "r")

    position = 0
    aim = 0
    depth = 0
    for line in file:
        (command, amount) = line.split(" ")
        if command == "forward":
            position += int(amount)
            depth += aim * int(amount)
        elif command == "up":
            aim -= int(amount)
        elif command == "down":
            aim += int(amount)

    print(position * depth)



from timing import timing
import os
import sys


def both_parts():
    file = open(os.path.join(sys.path[0], "inputs/input_day13.txt"), "r")

    dots = set()
    first_fold = True
    for line in file:
        if line.startswith("fold"):
            (axis, value) = line.strip()[11:].split("=")
            value = int(value)
            if axis == "y":
                for dot in dots.copy():
                    (x, y) = dot
                    if y > value:
                        new_dot_coord = (x, y - ((y - value) * 2))
                        dots.remove(dot)
                        if new_dot_coord not in dots:
                            dots.add(new_dot_coord)
            elif axis == "x":
                for dot in dots.copy():
                    (x, y) = dot
                    if x > value:
                        dots.remove(dot)
                        dots.add((x - ((x - value) * 2), y))

            if first_fold:
                first_fold = False
                print(len(dots))
                timing.log("Part 1 finished!")
        elif line.strip():
            (x, y) = line.strip().split(",")
            dots.add((int(x), int(y)))

    max_x = 0
    max_y = 0
    for dot in dots:
        (x, y) = dot
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            char_to_print = "."
            if (x, y) in dots:
                char_to_print = "#"
            print(char_to_print, end='')
        print()


def part1():
    both_parts()


def part2():
    both_parts()


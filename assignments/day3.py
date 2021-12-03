import math

from timing import timing
import os
import sys
import numpy
from operator import add
from functools import reduce

def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day3.txt"), "r")

    counts = reduce(add, list(map(lambda linje: numpy.array(list(map(int, list(linje.strip() + "1")))), file.readlines())))

    total_lines = counts[len(counts)-1]
    most_common = ""
    least_common = ""
    for count in counts[:-1]:
        common_bit = min(max(count - int(total_lines/2), 0), 1)
        most_common += str(common_bit)
        least_common += str((common_bit + 1) % 2)

    print(int(most_common, 2) * int(least_common, 2))


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day3.txt"), "r")


    numbers = list(map(lambda linje: numpy.array(list(map(int, list(linje.strip())))), file.readlines()))

    oxygen_numbers = numbers.copy()
    co2_numbers = numbers.copy()
    for i in range(len(oxygen_numbers[0])):
        new_oxygen = []
        new_co2 = []

        if len(oxygen_numbers) > 1:
            (least_common, most_common) = most_and_least_common(oxygen_numbers)
            for oxygen_candidate in oxygen_numbers:
                if oxygen_candidate[i] == most_common[i]:
                    new_oxygen.append(oxygen_candidate)

            oxygen_numbers = new_oxygen

        if len(co2_numbers) > 1:
            (least_common, most_common) = most_and_least_common(co2_numbers)
            for co2_candidate in co2_numbers:
                if co2_candidate[i] == least_common[i]:
                    new_co2.append(co2_candidate)

            co2_numbers = new_co2

    print(int(''.join([str(x) for x in oxygen_numbers[0]]), 2) * int(''.join([str(x) for x in co2_numbers[0]]), 2))


def most_and_least_common(numbers):
    counts = reduce(add, list(map(lambda number_list: numpy.append(number_list, [[1]]), numbers)))

    total_lines = counts[len(counts)-1]
    most_common = []
    least_common = []
    for count in counts[:-1]:
        if total_lines % 2 == 0 and count == total_lines / 2:
            common_bit = 1
        else:
            common_bit = min(max(count - int(total_lines / 2), 0), 1)
        most_common.append(common_bit)
        least_common.append((common_bit + 1) % 2)
    return least_common, most_common

from timing import timing
import os
import sys
import numpy

def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day3.txt"), "r")

    numbers = get_binary_array_from_file(file)

    (least_common, most_common) = least_and_most_common(sum(numbers), len(numbers))

    print(binary_array_to_decimal_number(least_common) * binary_array_to_decimal_number(most_common))


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day3.txt"), "r")

    oxygen_numbers = get_binary_array_from_file(file)
    co2_numbers = oxygen_numbers.copy()
    for i in range(len(oxygen_numbers[0])):
        if len(oxygen_numbers) > 1:
            (_, most_common) = least_and_most_common(sum(oxygen_numbers), len(oxygen_numbers))
            oxygen_numbers = list(filter(lambda candidate: candidate[i] == most_common[i], oxygen_numbers))

        if len(co2_numbers) > 1:
            (least_common, _) = least_and_most_common(sum(co2_numbers), len(co2_numbers))
            co2_numbers = list(filter(lambda candidate: candidate[i] == least_common[i], co2_numbers))

    print(binary_array_to_decimal_number(oxygen_numbers[0]) * binary_array_to_decimal_number(co2_numbers[0]))


def least_and_most_common(counts, total_numbers):
    most_common = [numpy.clip(count - (int(total_numbers / 2) - ((total_numbers + 1) % 2)), 0, 1) for count in counts]
    least_common = [(bin_num + 1) % 2 for bin_num in most_common]

    return least_common, most_common


def binary_array_to_decimal_number(binary_array):
    return int(''.join([str(x) for x in binary_array]), 2)


def get_binary_array_from_file(file):
    return [numpy.array([int(binary) for binary in line.strip()]) for line in file.readlines()]

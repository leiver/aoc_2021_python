from timing import timing
import os
import sys


def both_parts():
    file = open(os.path.join(sys.path[0], "inputs/input_day14.txt"), "r")

    polymer, rules = file.read().split("\n\n")
    rules = {pair: middle for pair, middle in [rule.strip().split(" -> ") for rule in rules.split("\n")]}
    pairs = {}
    for first, last in zip(polymer, polymer[1:]):
        pair = first + last
        pairs[pair] = pairs.get(pair, 0) + 1

    for step in range(40):
        if step == 10:
            sums_per_char = get_sums_per_char(pairs, polymer)
            print(max(sums_per_char.values()) - min(sums_per_char.values()))

            timing.log("Part 1 finished!")

        new_pairs = {}
        for pair, count in pairs.items():
            if pair in rules:
                first_new_pair = pair[0] + rules[pair]
                second_new_pair = rules[pair] + pair[1]
                new_pairs[first_new_pair] = new_pairs.get(first_new_pair, 0) + count
                new_pairs[second_new_pair] = new_pairs.get(second_new_pair, 0) + count
            else:
                new_pairs[pair] = new_pairs.get(pair, 0) + count

        pairs = new_pairs

    sums_per_char = get_sums_per_char(pairs, polymer)

    print(max(sums_per_char.values()) - min(sums_per_char.values()))


def get_sums_per_char(pairs, polymer):
    sums_per_char = {}
    for pair, count in pairs.items():
        sums_per_char[pair[0]] = sums_per_char.get(pair[0], 0) + count
    sums_per_char[polymer[-1]] = sums_per_char.get(polymer[-1], 0) + 1
    return sums_per_char


def part1():
    both_parts()


def part2():
    both_parts()


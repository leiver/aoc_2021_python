import math

from timing import timing
import os
import sys
from itertools import permutations
from copy import deepcopy


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day18.txt"), "r")

    line = file.readline().strip()
    snail_sum, _ = parse_snail_pair(None, line)
    for line in file:
        next_snail_pair, _ = parse_snail_pair(None, line.strip())

        snail_sum = add_pairs_together(snail_sum, next_snail_pair)

    print(sum_numbers_in_pair(snail_sum))


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day18.txt"), "r")

    snail_pairs = []
    for line in file:
        pair, _ = parse_snail_pair(None, line.strip())
        snail_pairs.append(pair)

    snail_pair_combinations = list(permutations(snail_pairs, 2))

    largest_snail_sum = 0
    for snail_pair_combination in snail_pair_combinations:
        first_snail_pair, second_snail_pair = snail_pair_combination
        largest_snail_sum = max(largest_snail_sum, sum_numbers_in_pair(add_pairs_together(deepcopy(first_snail_pair), deepcopy(second_snail_pair))))

    print(largest_snail_sum)

def sum_numbers_in_pair(snail_pair):
    result = 0
    if isinstance(snail_pair.left, SnailPair):
        result += 3 * sum_numbers_in_pair(snail_pair.left)
    elif isinstance(snail_pair.left, int):
        result += 3 * snail_pair.left
    if isinstance(snail_pair.right, SnailPair):
        result += 2 * sum_numbers_in_pair(snail_pair.right)
    elif isinstance(snail_pair.right, int):
        result += 2 * snail_pair.right
    return result


def add_pairs_together(left_pair, right_pair):
    added_pair = SnailPair(None, left_pair, right_pair)
    left_pair.parent = added_pair
    right_pair.parent = added_pair

    while True:
        exploded = explode_first_pair(added_pair)
        if not exploded:
            split = split_first_pair(added_pair)
            if not split:
                break

    return added_pair


def explode_first_pair(root):
    exploding_pair = find_exploding_pair(root, 0)
    if not exploding_pair:
        return False

    last = exploding_pair
    current = exploding_pair.parent
    while True:
        if current is None:
            break
        if last == current.right:
            if isinstance(current.left, SnailPair):
                current = current.left
                while isinstance(current.right, SnailPair):
                    current = current.right
                current.right += exploding_pair.left
                break
            else:
                current.left += exploding_pair.left
                break
        else:
            last = current
            current = current.parent
    last = exploding_pair
    current = exploding_pair.parent
    while True:
        if current is None:
            break
        if last == current.left:
            if isinstance(current.right, SnailPair):
                current = current.right
                while isinstance(current.left, SnailPair):
                    current = current.left
                current.left += exploding_pair.right
                break
            else:
                current.right += exploding_pair.right
                break
        else:
            last = current
            current = current.parent

    if exploding_pair.parent.left == exploding_pair:
        exploding_pair.parent.left = 0
    else:
        exploding_pair.parent.right = 0

    return True


def find_exploding_pair(pair, level):
    if level >= 4 and isinstance(pair.left, int) and isinstance(pair.right, int):
        return pair
    exploding_pair = None
    if isinstance(pair.left, SnailPair):
        exploding_pair = find_exploding_pair(pair.left, level + 1)
    if not exploding_pair and isinstance(pair.right, SnailPair):
        exploding_pair = find_exploding_pair(pair.right, level + 1)
    return exploding_pair


def split_first_pair(pair):
    if isinstance(pair.left, SnailPair):
        if split_first_pair(pair.left):
            return True
    elif isinstance(pair.left, int) and pair.left > 9:
        pair.left = SnailPair(pair, int(pair.left / 2), math.ceil(pair.left / 2))
        return True
    if isinstance(pair.right, SnailPair):
        if split_first_pair(pair.right):
            return True
    elif isinstance(pair.right, int) and pair.right > 9:
        pair.right = SnailPair(pair, int(pair.right / 2), math.ceil(pair.right / 2))
        return True

    return False


def parse_snail_pair(parent, line, level=0):
    pair = SnailPair(parent)
    line = line[1:]
    if line[0] == "[":
        left, line = parse_snail_pair(pair, line, level + 1)
        pair.left = left
    else:
        pair.left = int(line[0])
        line = line[1:]
    line = line[1:]

    if line[0] == "[":
        right, line = parse_snail_pair(pair, line, level + 1)
        pair.right = right
    else:
        pair.right = int(line[0])
        line = line[1:]

    return pair, line[1:]




class SnailPair:
    def __init__(self, parent, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.left},{self.right}]"

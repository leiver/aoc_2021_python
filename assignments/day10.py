from timing import timing
import os
import sys
from collections import deque
from statistics import median
from functools import reduce

bracket_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
bracket_scores_corrupt = {")": 3, "]": 57, "}": 1197, ">": 25137}
bracket_scores_incomplete = {"(": 1, "[": 2, "{": 3, "<": 4}


def both_parts():
    file = open(os.path.join(sys.path[0], "inputs/input_day10.txt"), "r")
    corrupt_score = 0
    incomplete_scores = []
    for line in file:
        stack = deque()
        corrupt = False
        for bracket in line.strip():
            if bracket in bracket_map.keys():
                stack.append(bracket)
            else:
                starting_bracket = stack.pop() if len(stack) > 0 else None
                if not starting_bracket or bracket_map[starting_bracket] != bracket:
                    corrupt_score += bracket_scores_corrupt[bracket]
                    corrupt = True
                    break

        if not corrupt and len(stack) > 0:
            incomplete_scores.append(reduce(lambda score, next_bracket: (score * 5) + bracket_scores_incomplete[next_bracket], reversed(stack), 0))

    print(corrupt_score)

    timing.log("Part 1 finished!")

    print(int(median(incomplete_scores)))


def part1():
    both_parts()


def part2():
    both_parts()


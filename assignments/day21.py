from timing import timing
import os
import sys


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day21.txt"), "r")

    player_pos = [9, 6]
    player_score = [0, 0]
    dice = 1
    current_player = 0
    dice_rolls = 0

    while player_score[0] < 1000 and player_score[1] < 1000:
        player_pos[current_player] += dice -1
        dice = (dice % 100) + 1
        player_pos[current_player] += dice
        dice = (dice % 100) + 1
        player_pos[current_player] += dice
        dice = (dice % 100) + 1
        player_pos[current_player] = (player_pos[current_player] % 10) + 1

        player_score[current_player] += player_pos[current_player]
        current_player = (current_player + 1) % 2
        dice_rolls += 3

    print(min(player_score) * dice_rolls)


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day21.txt"), "r")


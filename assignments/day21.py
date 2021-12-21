from timing import timing
from itertools import permutations
from collections import Counter
import json


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
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
    dice_permutations = dict(Counter(map(sum, set(permutations([1, 1, 1, 2, 2, 2, 3, 3, 3], 3)))))

    players = {
        1: initialize_player(9),
        2: initialize_player(6)
    }

    turn = 1
    finished = False
    while not finished:
        for player, turns in players.items():
            last_turn = turns[turn - 1]
            if last_turn["ongoing timelines"] == 0:
                finished = True
            next_turn_positions = {}
            ongoing_timelines = 0
            winning_timelines = 0
            for position, scores in last_turn["positions"].items():
                for dice_result, splits in dice_permutations.items():
                    next_position = ((position + dice_result - 1) % 10) + 1
                    scores_to_update = next_turn_positions.get(next_position, {})
                    for score, timelines in scores.items():
                        new_score = score + next_position
                        new_timelines = timelines * splits
                        if new_score >= 21:
                            winning_timelines += new_timelines
                        else:
                            ongoing_timelines += new_timelines
                            scores_to_update[new_score] = scores_to_update.get(new_score, 0) + new_timelines
                    next_turn_positions[next_position] = scores_to_update
            turns.append({
                "positions": next_turn_positions,
                "ongoing timelines": ongoing_timelines,
                "winning timelines": winning_timelines
            })
        turn += 1

    player_1_winning_timelines = 0
    player_2_winning_timelines = 0
    for turn in range(1, max(len(players[1]), len(players[2]))):
        player_1_winning_timelines += players[1][turn]["winning timelines"] * players[2][turn - 1]["ongoing timelines"]
        player_2_winning_timelines += players[2][turn - 1]["winning timelines"] * players[1][turn]["ongoing timelines"]

    print(max(player_1_winning_timelines, player_2_winning_timelines))


def initialize_player(starting_position):
    return [
        {
            "positions": {
                starting_position: {
                    0: 1
                }
            },
            "ongoing timelines": 1,
            "winning timelines": 0
        }
    ]

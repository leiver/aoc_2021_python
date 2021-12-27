import json

from timing import timing
import os
import sys
from itertools import combinations


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day22.txt"), "r")

    active_cubes = set()

    for line in file:
        action, coords = line.strip().split(" ")
        x_ranges, y_ranges, z_ranges = [tuple(map(int, coord[2:].split(".."))) for coord in coords.split(",")]
        if in_bounds(x_ranges) and in_bounds(y_ranges) and in_bounds(z_ranges):
            for x in range(x_ranges[0], x_ranges[1] + 1):
                for y in range(y_ranges[0], y_ranges[1] + 1):
                    for z in range(z_ranges[0], z_ranges[1] + 1):
                        if action == "on":
                            active_cubes.add((x, y, z))
                        else:
                            active_cubes.discard((x, y, z))

    print(len(active_cubes))


def in_bounds(coord_range):
    return -50 <= coord_range[0] and 50 >= coord_range[1]


def part2():
    file = open(os.path.join(sys.path[0], "inputs/tests/input_day22_test.txt"), "r")

    actions = []
    for line in file:
        action, coords = line.strip().split(" ")
        x_ranges, y_ranges, z_ranges = [tuple(map(int, coord[2:].split(".."))) for coord in coords.split(",")]
        actions.append((action, x_ranges, y_ranges, z_ranges))

    #for action in actions:
        #print(action)
    total_active_cubes = 0
    for step, (action, x_ranges, y_ranges, z_ranges) in enumerate(actions):
        if action == "on":
            print(f"parsing step {step}: {action}, {x_ranges}, {y_ranges}, {z_ranges}")
            if step == len(actions) - 1:
                cubes_to_remove_from_later_actions = 0
            else:
                #print(actions[step+1:])
                actions_affecting_current_action = []
                for parsed_action, parsed_x_ranges, parsed_y_ranges, parsed_z_ranges in actions[step+1:]:
                    if cube_in_bound(x_ranges, y_ranges, z_ranges, parsed_x_ranges, parsed_y_ranges, parsed_z_ranges):
                        print(f"\tadding {parsed_action, parsed_x_ranges, parsed_y_ranges, parsed_z_ranges}")
                        actions_affecting_current_action.append((parsed_action, parsed_x_ranges, parsed_y_ranges, parsed_z_ranges))
                    else:
                        print(f"\t\tremoving {parsed_action, parsed_x_ranges, parsed_y_ranges, parsed_z_ranges}")
                action_combinations = []
                if len(actions_affecting_current_action) == 1:
                    action_combinations = [(1, [[action] for action in actions_affecting_current_action])]
                elif len(actions_affecting_current_action) > 1:
                    action_combinations = [(1, [[action] for action in actions_affecting_current_action])] + [
                        (number_of_combinations, list(combinations(actions_affecting_current_action, number_of_combinations)))
                        for number_of_combinations
                        in range(2, len(actions_affecting_current_action))
                    ]
                #print(json.dumps(action_combinations, sort_keys=True, indent=4))
                cubes_to_remove_from_later_actions = 0
                for number_of_combinations, list_of_combinations in action_combinations:
                    #print(f"\tparsing number of combinations: {number_of_combinations}")
                    total_number_of_cubes_in_list_of_combinations = 0
                    for combination in list_of_combinations:
                        #print(f"\t\tparsing combination {combination}")
                        number_of_cubes_in_combination = (max(min([x_ranges[1] + 1] + [x[1] + 1 for _, x, _, _ in combination]) - max([x_ranges[0]] + [x[0] for _, x, _, _ in combination]), 0) *
                                                          max(min([y_ranges[1] + 1] + [y[1] + 1 for _, _, y, _ in combination]) - max([y_ranges[0]] + [y[0] for _, _, y, _ in combination]), 0) *
                                                          max(min([z_ranges[1] + 1] + [z[1] + 1 for _, _, _, z in combination]) - max([z_ranges[0]] + [z[0] for _, _, _, z in combination]), 0))
                        #print(f"\t\tnumber_of_cubes_in_combination: {number_of_cubes_in_combination}")
                        total_number_of_cubes_in_list_of_combinations += number_of_cubes_in_combination
                    total_number_of_cubes_in_list_of_combinations *= 1 if number_of_combinations % 2 else -1
                    #print(f"\tadding to cubes_to_remove_from_later_actions: {total_number_of_cubes_in_list_of_combinations}")
                    cubes_to_remove_from_later_actions += total_number_of_cubes_in_list_of_combinations
                #print(f"cubes_to_remove_from_later_actions: {cubes_to_remove_from_later_actions}")
                #cubes_to_remove_from_later_actions = sum([
                #    sum([
                #        max(min([x_ranges[1]] + [x[1] for _, x, _, _ in combination]) - max([x_ranges[0]] + [x[0] for _, x, _, _ in combination]), 0) *
                #        max(min([y_ranges[1]] + [y[1] for _, _, y, _ in combination]) - max([y_ranges[0]] + [y[0] for _, _, y, _ in combination]), 0) *
                #        max(min([z_ranges[1]] + [z[1] for _, _, _, z in combination]) - max([z_ranges[0]] + [z[0] for _, _, _, z in combination]), 0)
                #        for combination
                #        in list_of_combinations
                #    ]) * (1 if number_of_combinations % 2 else -1)
                #    for number_of_combinations, list_of_combinations
                #    in action_combinations
                #])

            cubes_from_step = (x_ranges[1]+1 - x_ranges[0]) * (y_ranges[1]+1 - y_ranges[0]) * (z_ranges[1]+1 - z_ranges[0])
            #print(f"cubes_from_step: {cubes_from_step}")
            cubes_to_add = cubes_from_step - cubes_to_remove_from_later_actions
            #print(f"cubes_to_add: {cubes_to_add}")
            print()
            total_active_cubes += cubes_to_add

    print(total_active_cubes)


def cube_in_bound(x_ranges, y_ranges, z_ranges, parsed_x_ranges, parsed_y_ranges, parsed_z_ranges):
    return (parsed_x_ranges[0] <= x_ranges[1] and parsed_x_ranges[1] >= x_ranges[0]
            and parsed_y_ranges[0] <= y_ranges[1] and parsed_y_ranges[1] >= y_ranges[0]
            and parsed_z_ranges[0] <= z_ranges[1] and parsed_z_ranges[1] >= z_ranges[0])


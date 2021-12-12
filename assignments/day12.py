from timing import timing
import os
import sys


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day12.txt"), "r")

    paths = get_paths_from_file(file)

    print(paths_to_end_part_1("start", paths, set()))


def paths_to_end_part_1(current_node, paths, traversed_paths):
    if current_node.islower():
        traversed_paths.update({current_node})
    paths_got_to_end = 0
    for next_node in paths[current_node]:
        if next_node == "end":
            paths_got_to_end += 1
        elif next_node not in traversed_paths:
            paths_got_to_end += paths_to_end_part_1(next_node, paths, traversed_paths)
    if current_node.islower():
        traversed_paths.remove(current_node)
    return paths_got_to_end


def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day12.txt"), "r")

    paths = get_paths_from_file(file)

    print(paths_to_end_part_2("start", paths, set(), False))


def paths_to_end_part_2(current_node, paths, traversed_nodes, traversed_node_twice):
    traversed_this_node_twice = False
    if current_node.islower():
        if current_node in traversed_nodes:
            traversed_node_twice = True
            traversed_this_node_twice = True
        else:
            traversed_nodes.add(current_node)

    paths_got_to_end = 0
    for next_node in paths[current_node]:
        if next_node == "end":
            paths_got_to_end += 1
        elif (not traversed_node_twice or next_node not in traversed_nodes) and next_node != "start":
            paths_got_to_end += paths_to_end_part_2(next_node, paths, traversed_nodes, traversed_node_twice)

    if not traversed_this_node_twice:
        traversed_nodes.discard(current_node)

    return paths_got_to_end


def get_paths_from_file(file):
    paths = {}
    for line in file:
        (from_node, to_node) = line.strip().split("-")
        paths[from_node] = paths.get(from_node, []) + [to_node]
        paths[to_node] = paths.get(to_node, []) + [from_node]
    return paths


from timing import timing
import os
import sys


def both_parts():
    part1()

    timing.log("Part 1 finished!")

    part2()


def part1():
    file = open(os.path.join(sys.path[0], "inputs/input_day4.txt"), "r")

    bingo_numbers = file.readline().strip().split(",")
    file.readline()

    bingo_boards = get_boards_from_file(file)
    winning_board = None

    for bingo_number in bingo_numbers:
        for board in bingo_boards:
            for row_index in range(len(board["rows"])):
                for column_index in range(len(board["columns"])):
                    row = board["rows"][row_index]
                    if column_index in row and row[column_index] == bingo_number:
                        column = board["columns"][column_index]
                        del row[column_index]
                        del column[row_index]

                        if not row or not column:
                            winning_board = board

            if winning_board:
                break
        if winning_board:
            print(int(bingo_number) * sum([sum([int(number) for number in row.values()]) for row in winning_board["rows"]]))
            break



def part2():
    file = open(os.path.join(sys.path[0], "inputs/input_day4.txt"), "r")

    bingo_numbers = file.readline().strip().split(",")
    file.readline()

    bingo_boards = get_boards_from_file(file)
    winning_board = None
    won_boards = []

    for bingo_number in bingo_numbers:
        for board in bingo_boards:
            if board not in won_boards:
                for row_index in range(len(board["rows"])):
                    for column_index in range(len(board["columns"])):
                        row = board["rows"][row_index]
                        if column_index in row and row[column_index] == bingo_number:
                            column = board["columns"][column_index]
                            del row[column_index]
                            del column[row_index]

                            if not row or not column:
                                winning_board = board

                if winning_board == board:
                    won_boards.append(board)
        if len(won_boards) == len(bingo_boards):
            break

    if winning_board:
        print(int(bingo_number) * sum([sum([int(number) for number in row.values()]) for row in winning_board["rows"]]))


def get_boards_from_file(file):
    bingo_boards = []
    current_board = {"columns": [], "rows": []}
    current_row = 0
    for line in file.readlines():
        line = line.strip()
        if line:
            row_numbers = line.split()
            current_board["rows"].append({})
            for i in range(len(row_numbers)):
                current_board["rows"][current_row][i] = row_numbers[i]
                if current_row == 0:
                    current_board["columns"].append({current_row: row_numbers[i]})
                else:
                    current_board["columns"][i][current_row] = row_numbers[i]

            current_row += 1

        else:
            bingo_boards.append(current_board)
            current_board = {"columns": [], "rows": []}
            current_row = 0
    bingo_boards.append(current_board)
    return bingo_boards


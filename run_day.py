import sys, os
import re

if __name__ == '__main__':
    file_regex = re.compile('^day([0-9]*).py$')
    filenames = next(os.walk(os.getcwd() + "/assignments"), (None, None, []))[2]
    day_numbers = map(lambda matched_file: matched_file.group(1), filter(None, map(lambda file_name: file_regex.match(file_name), filenames)))

    if len(sys.argv) >= 2 and sys.argv[1].isnumeric() and sys.argv[1] in day_numbers:
        import_name = "day" + sys.argv[1]
        imported = getattr(__import__("assignments", fromlist=[import_name]), import_name)

        if len(sys.argv) >= 3 and sys.argv[2] == "1":
            imported.part1()
        elif len(sys.argv) >= 3 and sys.argv[2] == "2":
            imported.part2()
        else:
            imported.both_parts()
    else:
        print("First argument needs to be a valid day number with a corresponding script under assignments/day<#>.py")

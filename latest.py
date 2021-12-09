import sys, os
import re
from timing import timing

if __name__ == '__main__':
    file_regex = re.compile('^day([0-9]*).py$')
    filenames = next(os.walk(os.getcwd() + "/assignments"), (None, None, []))[2]
    day_numbers = map(lambda matched_file: int(matched_file.group(1)), filter(None, map(lambda file_name: file_regex.match(file_name), filenames)))

    day = max(day_numbers)
    if day:
        import_name = "day" + str(day)
        imported = getattr(__import__("assignments", fromlist=[import_name]), import_name)

        timing.log("*** Starting day {0}! ***".format(day))

        if len(sys.argv) >= 2 and sys.argv[1] == "1":
            imported.part1()
        elif len(sys.argv) >= 2 and sys.argv[1] == "2":
            imported.part2()
        else:
            imported.both_parts()

        timing.log("*** Day {0} finished! ***".format(day))


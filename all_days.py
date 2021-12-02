import os
import re
import timing

if __name__ == '__main__':
    timing.log("Starting to run all days!")

    file_regex = re.compile('^day([0-9]*).py$')
    filenames = next(os.walk(os.path.dirname(__file__) + "/assignments"), (None, None, []))[2]
    day_numbers = map(lambda matched_file: int(matched_file.group(1)), filter(None, map(lambda file_name: file_regex.match(file_name), filenames)))

    for day in map(str, sorted(day_numbers)):
        timing.log("*** Starting day {0}! ***".format(day))

        import_name = "day" + day
        imported = getattr(__import__("assignments", fromlist=[import_name]), import_name)
        imported.both_parts()

        timing.log("*** Day {0} finished! ***".format(day))

    timing.log("Finished running all days!")

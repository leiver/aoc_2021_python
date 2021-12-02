import os
import re

if __name__ == '__main__':
    file_regex = re.compile('^day([0-9]*).py$')
    filenames = next(os.walk(os.path.dirname(__file__) + "/assignments"), (None, None, []))[2]
    day_numbers = map(lambda matched_file: int(matched_file.group(1)), filter(None, map(lambda file_name: file_regex.match(file_name), filenames)))

    day = max(day_numbers)
    if day:
        import_name = "day" + str(day)
        imported = getattr(__import__("assignments", fromlist=[import_name]), import_name)
        imported.both_parts()


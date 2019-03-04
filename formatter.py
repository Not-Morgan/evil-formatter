#!/usr/bin/python

import sys
import re

end_characters = ";{}" # all the characters to be moved
# regex makes five groups: [indentation, end_chars, body, idk, end_chars, body]
# most are optional and will have the value None when checked
# regex = "([ \t]*)?([{0}]+)?([^{0}]+)([{0}]+)?(.*)$".format(end_characters)
regex = "([ \t]*)?([;{}]+)?(([^;{}]|[;{}](?=.*\))|{(?=.*}))+)([;{} ]+)?(.*)$"
delete_lines = []

file_name = sys.argv[1]
with open(file_name, 'r') as f:
    file = list(f)

# replace tabs with spaces so line length is consistent
for line in range(len(file)):
    file[line] = file[line].replace("\t", "    ")

# place the column of characters after the longest line
padding = max(len(i) for i in file)

lastLine = 0  # the last line containing non end characters
for n, line in enumerate(file):
    if any(c not in end_characters for c in line.strip()):

        if sum([line.count(c) for c in end_characters]) > 0:
            # split line into regex groups
            match = re.match(regex, line)

            # if there are end characters at the beginning put them on the previous line
            if match[2]:
                file[lastLine] += match[2]

            # the main part which doesn't move after
            body = ""
            # indentation
            if match[1]:
                body += match[1]
            # main part before
            if match[3]:
                body += match[3]
            # any text like comments after the last end characters
            if match[6]:
                body += match[6]

            file[n] = body.ljust(padding)
            if match[5]:
                file[n] += match[5]
            file[n] += '\n'

        else:
            file[n] = file[n][:-1].ljust(padding) + '\n'

        lastLine = n

    elif line.strip() != "":
        # if a line is just end characters move it to the last normal line
        file[lastLine] = file[lastLine][:-1] + line.strip() + '\n'
        # mark the moved line to be deleted
        delete_lines.append(n)

# delete all the moved lines
for line in reversed(delete_lines):
    file.pop(line)

# strip trailing spaces and add newlines
for line in range(len(file)):
    file[line] = file[line].rstrip() + '\n'

with open(file_name, "w") as f:
    f.write("".join(file))

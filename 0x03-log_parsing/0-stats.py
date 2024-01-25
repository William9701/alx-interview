#!/usr/bin/python3
"""This script reads lines from stdin in this format
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
and after every 10 lines or keyboard interruption
it prints File size: <total size>
<status code>: <number> for every status code"""

from sys import stdin
import re

container = {}
total_size = 0


def format_check(line):
    """checks if the line have a valid format"""
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)
    if match:
        return True
    return False


try:
    container = {}
    total_size = 0
    for i, line in enumerate(stdin, start=1):
        line = line.strip()
        if not format_check(line):
            continue
        args = line.split(" ")
        total_size += int(args[-1])
        if args[-2] not in container:
            container[args[-2]] = 1
        else:
            container[args[-2]] += 1
        container = dict(sorted(container.items()))
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, val in container.items():
                print(f"{key}: {val}")
except Exception as err:
    pass
finally:
    print(f"File size: {total_size}")
    for key, val in container.items():
        print(f"{key}: {val}")

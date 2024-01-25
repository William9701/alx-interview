#!/usr/bin/python3
""" this is the log passing count"""
import sys


def print_metrics(total_size, status_codes):
    """
    Print statistics
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """
    Parse a log line and update statistics
    """
    tokens = line.split(" ")
    if len(tokens) > 2:
        status_code = tokens[-2]
        if status_code.isnumeric():
            total_size += int(tokens[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1
    return total_size, status_codes


if __name__ == "__main__":
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size, status_codes = parse_line(
                line.strip(), total_size, status_codes)

            if i % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

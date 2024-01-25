#!/usr/bin/python3
""" this is the log passing count"""
import sys
import re
import signal

# Initialize counters
total_file_size = 0
status_code_counts = {str(code): 0 for code in
                      [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

# Regular expression pattern for the log format
pattern = r'^(?P<ip>\S+) - \[(?P<date>.+)\] "GET /projects/260 HTTP/1.1" ' \
          r'(?P<status>\d{3}) (?P<size>\d+)$'


def print_metrics(signal=None, frame=None):
    print("File size: ", total_file_size)
    for status, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status}: {count}")


# Register the signal handler
signal.signal(signal.SIGINT, print_metrics)

try:
    for line in sys.stdin:
        match = re.match(pattern, line.strip())
        if match:
            data = match.groupdict()
            total_file_size += int(data['size'])
            if data['status'] in status_code_counts:
                status_code_counts[data['status']] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    pass
finally:
    print_metrics()

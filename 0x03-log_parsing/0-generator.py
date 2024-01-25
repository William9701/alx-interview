#!/usr/bin/python3
"""This is a log passng count"""
import sys
import signal

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

# Function to handle keyboard interruption
def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
for line in sys.stdin:
    try:
        # Parse log entry
        parts = line.split()
        ip_address, date, method, status_code, file_size = parts[0], parts[3][1:], parts[5][1:], int(parts[8]), int(parts[9])

        # Check if the method is "GET" and update metrics
        if method == "GET":
            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_statistics()

    except (IndexError, ValueError):
        # Skip the line if the format is not as expected
        pass


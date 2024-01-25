#!/usr/bin/python3
import sys
from collections import defaultdict

def print_stats(total_size, status_code_counts):
    """
    Print the current statistics, including total file size and status code counts.

    Args:
    - total_size (int): Total file size.
    - status_code_counts (dict): Dictionary containing counts of different status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_code_counts):
        print("{}: {}".format(code, status_code_counts[code]))

def main():
    """
    Main function to read input from stdin, compute metrics, and print statistics.
    """
    total_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Check if the line follows the specified format
            if len(parts) != 7 or parts[2] != "GET" or parts[3] != "/projects/260" or parts[4] != "HTTP/1.1":
                continue

            try:
                file_size = int(parts[6])
                status_code = int(parts[5])

                total_size += file_size
                status_code_counts[status_code] += 1

            except ValueError:
                pass

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_code_counts)

    except KeyboardInterrupt:
        pass  # Handle KeyboardInterrupt to print final statistics

    print_stats(total_size, status_code_counts)

if __name__ == "__main__":
    main()


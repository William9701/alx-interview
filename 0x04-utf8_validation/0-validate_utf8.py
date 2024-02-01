#!/usr/bin/python3
"""
utf8 main file for testing
"""


def validUTF8(data):
    """"This method for the testing"""
    count = 0
    for num in data:
        bin_rep = format(num, '#010b')[-8:]  # Get the binary
        # representation of the number
        if count == 0:  # If this is the start of a new character
            for bit in bin_rep:
                if bit == '0':
                    break
                count += 1
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:  # If this is not the first byte of a character
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        count -= 1
    return count == 0

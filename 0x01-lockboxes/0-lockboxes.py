#!/usr/bin/python3
""" This is a module that unlocks boxes"""


def canUnlockAll(boxes):
    """ this is the method that unlocks boxes"""
    unlocked = {0}  # Step 1: Initialize the set of unlocked boxes with box 0
    stack = [0]  # Use a stack to keep track of boxes to process

    while stack:  # Step 3: Repeat until no new boxes can be unlocked
        box = stack.pop()
        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):  # Only process valid and locked boxes
                unlocked.add(key)  # Unlock the box
                stack.append(key)  # Add the box to the stack to process its keys

    # Step 4: Check if all boxes have been unlocked
    return len(unlocked) == len(boxes)

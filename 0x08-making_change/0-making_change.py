#!/usr/bin/python3
"""
makeChange module
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (List[int]): A list of the values of the coins in your possession.
    total (int): The total amount to meet.

    Returns:
    int: The fewest number of coins  less, return 0.
         If total cannot bve, return -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        num, total = divmod(total, coin)
        count += num

    return count if total == 0 else -1

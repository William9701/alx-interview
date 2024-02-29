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
    int: The fewest number of coins needed to meet total. If total is 0 or less, return 0.
         If total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

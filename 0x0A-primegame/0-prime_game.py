#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines the winner of the game"""
    if not nums or x < 1 or x < len(nums):
        return None

    n = max(nums)
    primes = [False, False] + [True for _ in range(2, n+1)]
    p = 2

    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    Maria_wins = sum(sum(primes[:num+1]) % 2 != 0 for num in nums)
    Ben_wins = x - Maria_wins

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None

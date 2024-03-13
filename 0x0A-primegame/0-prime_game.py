#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines if a player is the winner"""
    if x is None or nums is None or len(nums) == 0:
        return None
    if x < 1:
        return None
    if x < len(nums):
        return None

    p, n = 2, max(nums)
    b_win, m_win = 0, 0
    primes = [True for i in range(n + 1)]

    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    for ele in nums:
        prime = 0
        for i in range(2, ele + 1):
            if primes[i]:
                prime += 1
        if prime % 2 == 0:
            b_win += 1
        else:
            m_win += 1

    if b_win > m_win:
        return "Ben"
    if b_win < m_win:
        return "Maria"
    return None

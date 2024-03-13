#!/usr/bin/python3
"""This is the prime game module"""


def isWinner(x, nums):
    """This is the IsWInner method"""
    def is_prime(n):
        """method to check if its prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def game(n):
        """This is the game method"""
        primes = [is_prime(i) for i in range(2, n+1)]
        return sum(primes) % 2 == 1

    Maria_wins = sum(game(n) for n in nums)
    Ben_wins = x - Maria_wins

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None

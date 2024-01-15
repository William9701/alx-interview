#!/usr/bin/python3
""" this  is minOperation module"""


def minOperations(n):
    """ This method solves the problem  by finding the prime factors
    of the number n. The minimum number of operations needed to get n
    ‘H’ characters is the sum of the prime factors of n"""
    operations = 0
    p = 2

    while n > 1:
        while n % p == 0:
            operations += p
            n //= p
        p += 1

    return operations

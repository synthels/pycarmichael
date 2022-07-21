#!/usr/bin/env python3

def is_squarefree(primes):
    for m in primes.values():
        if m > 1:
            return False
    return True


def is_carmichael(n, primes):
    for p in primes.keys():
        if ((n-1) % (p-1)) != 0:
            return False

    return (n % 2 == 1)

#!/usr/bin/env python3

import csv
import numpy as np

from sympy.ntheory import factorint, isprime
from .utils import is_squarefree, is_carmichael

# Upper search bound
upper_bound = 4*10**7


def main():
    gap = 0
    with open('gaps/data.csv', 'w', newline='') as csvfile:
        fields = ['x', 'G(x)']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for n in range(1, upper_bound + 1):
            primes = factorint(n)
            if isprime(n) or not is_squarefree(primes):
                continue

            if is_carmichael(n, primes):
                gap += 1
                writer.writerow({'x': n, 'G(x)': gap})
                gap = 0

            print(f"Checked {n}...")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import csv
import numpy as np

from sympy.ntheory import factorint, isprime

# Upper search bound
upper_bound = 3*10**7


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


def main():
    count = 0
    with open('counting-function/data.csv', 'w', newline='') as csvfile:
        fields = ['x', 'C(x)', 'log(x)']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for n in range(1, upper_bound + 1):
            primes = factorint(n)
            if isprime(n) or not is_squarefree(primes):
                continue

            if is_carmichael(n, primes):
                count += 1
                writer.writerow({'x': n, 'C(x)': count, 'log(x)': np.log(n)})

            print(f"Checked {n}...")


if __name__ == "__main__":
    main()

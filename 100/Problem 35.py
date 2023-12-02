'''
Circular Primes

The number, 197, is called circular prime because all rotations of the digits, 197, 971, and 719, are themselved prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 and 97.

How many circular primes are there below one million?
'''

import itertools


def p35():
    primes = find_primes(1_000_000)

    circular_primes = []
    # print(circular(197, primes))

    for p in primes:  # type: ignore
        cp = circular(p, primes)
        if not cp:
            continue
        for i in cp:
            if i not in circular_primes:
                circular_primes.append(i)
    print(len(circular_primes))


def circular(n, primes):
    combos = []
    digit = [d for d in str(n)]

    for s in range(len(digit)):
        if int("".join(digit)) not in primes:
            return False
        combos.append("".join(digit))
        digit.append(digit.pop(0))

    return combos


def find_primes(n):
    if n == 2:
        return True
    primes = []
    sieve = [True for _ in range(n)]
    for i in range(2, n+1):
        for id, p in enumerate(range(i, n, i)):
            if id == 0 and sieve[p-1]:
                primes.append(p)
            sieve[p-1] = False

    return primes


def main():
    p35()


if __name__ == '__main__':
    main()

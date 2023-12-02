'''
Truncatable Primes

The number 3797 has an interestng property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97 and 7. Similarly we can work from right to left: 3797, 379, 37 and 3.

Find the sum of the only eleven primes that are both truncutable from left to right and right to left.

NOTE: 2, 3, 5 and 7 are not considered to be truncutable primes
'''


def p37():
    LIMIT = 1_000_000
    primes = find_primes(LIMIT)
    truncs = []

    for p in primes:
        if p in [2, 3, 5, 7]:
            continue
        if int(str(p)[-1]) not in [2, 3, 5, 7]:
            continue
        if truncutable(p, primes):
            truncs.append(p)
        if len(truncs) >= 11:
            break
    print(sum(truncs))


def truncutable(p, primes):
    tr = False
    p = str(p)

    test_lr = all([int(p[i:]) in primes for i in range(len(str(p)))])
    test_rl = all([int(p[:i+1]) in primes for i in range(len(str(p)))])

    if all([test_rl, test_lr]):
        tr = True

    return tr


def find_primes(n):
    sieve = [True] * n
    for i in range(2, int(n**0.5+1)):
        if sieve[i-1]:
            for j in range(i*i, n+1, i):
                sieve[j-1] = False

    primes = [p+1 for p in range(1, n) if sieve[p]]

    return primes


def main():
    p37()


if __name__ == '__main__':
    main()

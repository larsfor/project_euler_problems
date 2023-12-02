'''
Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1+2+4+7+14=28, which means that is a perfect number.

A number is called deficient if the sum of its proper divisors is less than and it is called abundant if this sum exceeds

As 12 is the smallest abundant number, 1+2+3+4+6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 

By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

# from numba import jit
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def p23():
    # abundant = []
    # twoAbundant = []
    # nonAbundant = 0

    print("finding abundant numbers...")
    abundant = a()

    print("finding sum of two abundant numbers...")
    twoAbundant = b(abundant)

    print("finding integers which can't be written as a the sum of two abundant numbers...")
    nonAbundant = c(twoAbundant)

    print(nonAbundant)


# @jit
def a():
    abundant = np.empty(0)
    for n in range(28123):
        if find_pd(n) == "abundant":
            a = np.append(abundant, n)
            abundant = a
    return abundant


# @jit
def b(abundant):
    twoAbundant = np.empty(0)
    for x in abundant:
        for y in abundant:
            z = x+y
            if z not in twoAbundant:
                a = np.append(twoAbundant, z)
                twoAbundant = a
    return twoAbundant


# @jit
def c(twoAbundant):
    nonAbundant = 0
    for i in range(28123):
        if i not in twoAbundant:
            nonAbundant += i
    return nonAbundant


def find_pd(n):
    pSum = 0

    for i in range(1, n):
        if n % i == 0:
            pSum += i

    if n == pSum:
        status = 'perfect'

    elif n < pSum:
        status = 'abundant'

    else:
        status = 'deficient'
    return status


def main():
    p23()


if __name__ == '__main__':
    main()

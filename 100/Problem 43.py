'''
Sub-string Divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d(1) be the 1st digit, d(2) be the 2nd digit and so on. In this way, we note the following:
d2d3d4 = 406 is divisible by 2
d3d4d5 = 063 is divisible by 3
d4d5d6 = 635 is divisible by 5
d5d6d7 = 357 is divisible by 7
d6d7d8 = 572 is divisible by 11
d7d8d9 = 728 is divisible by 13
d8d9d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import itertools


def p41():
    # min_pan = 1234567891
    # # max_pan = 9876543210 + 1
    # max_pan = 4160357289 + 1
    # total = []
    # for n in range(min_pan, max_pan, 2):
    #     digits = '0123456789'
    #     # print(str(n))
    #     if "".join(sorted(str(n))) == digits:
    #         # print(n)
    #         d = divisible(n)
    #         if d:
    #             total.append(n)
    #             print(n)
    total = []
    pds = itertools.permutations('0123456789')
    for n in pds:
        digits = '0123456789'
        n = "".join(n)
        # print(n)
        if sorted(n) == digits:
            # print(n)
            d = divisible(n)
            if d:
                total.append(n)
                print(n)

    print(total)
    print(sum(total))


def divisible(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    strn = str(n)
    div = []
    for i in range(1, len(strn)-2):
        num = int(strn[i:i+3])
        div.append(num % primes[i-1] == 0)
    return all(div)


def main():
    p41()


if __name__ == '__main__':
    main()

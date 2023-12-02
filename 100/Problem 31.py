'''
Coin Sums

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins? 
'''


# from numba import jit


def p31():
    combs = combinations()
    print(combs)


# @jit(nopython=True)
def combinations():
    # a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0

    # count = 0
    # two_hundred = 0
    # s = set()

    # while True:
    #     if two_hundred == 200:
    #         break
    #     a += 1
    #     if h > 200:
    #         two_hundred += 1
    #     if g == 200:
    #         g = 0
    #         h += 200
    #     if f == 200:
    #         f = 0
    #         g += 100
    #     if e == 200:
    #         e = 0
    #         f += 50
    #     if d == 200:
    #         d = 0
    #         e += 20
    #     if c == 200:
    #         c = 0
    #         d += 10
    #     if b == 200:
    #         b = 0
    #         c += 5
    #     if a > 200:
    #         a = 0
    #         b += 2
    #     if sum([a, b, c, d, e, f, g, h]) == 200:
    #         # print(a, b, c, d, e, f, g, h)
    #         # count += 1
    #         s.add((a, b, c, d, e, f, g, h))

    # print(count)
    # return len(s)
    # return count
    s = set()

    for a in range(201):
        for b in range(101):
            for c in range(41):
                for d in range(21):
                    for e in range(11):
                        for f in range(5):
                            for g in range(3):
                                for h in range(2):
                                    if sum([a, 2*b, 5*c, 10*d, 20*e, 50*f, 100*g, 200*h]) == 200:
                                        s.add((a, 2*b, 5*c, 10*d, 20 *
                                              e, 50*f, 100*g, 200*h))

    return len(s)


def main():
    p31()


if __name__ == '__main__':
    main()

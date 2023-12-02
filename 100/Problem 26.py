'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1 digit recurring cycle. It can be seen that 1/7 has a 6 digit recurring cycle.
Find the value of d < 1000 for which 1/d contain the longst recurring cycle in it's decimal fraction part.
'''

from decimal import Context, setcontext, Decimal

myothercontext = Context(prec=100)
setcontext(myothercontext)


def p26():
    dMax = 0
    nMax = 0
    for n in range(1, 1001):
        d = find_decimal_repentends(n)
        if d > dMax:
            dMax = d
            nMax = n
        # print(d)
    print("dMax", dMax, "nMax", nMax)


def find_decimal_repentends(n):
    # based on the script here: https://oeis.org/A051626k
    lpow = 1
    while True:
        for mpow in range(lpow-1, -1, -1):
            if (10**lpow-10**mpow) % n == 0:
                return lpow-mpow
        lpow += 1


def main():
    p26()


if __name__ == '__main__':
    main()

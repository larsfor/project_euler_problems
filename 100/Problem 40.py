'''
Champernowne's Constant

An irrational decimal fraction is created by concatenating the positive integers:
                                0.12345678910[1]112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

if d(n) represents the nth digit of the fractional part, find the value of the following expression.

                            d(1) x d(10) x d(100) x d(1_000) x d(10_000) x d(100_000) x d(1_000_000)
'''


def p40():
    cc = ''
    for i in range(1_000_001):
        cc += str(i)
    # print(cc)
    d_1 = int(cc[1])
    d_10 = int(cc[10])
    d_100 = int(cc[100])
    d_1000 = int(cc[1000])
    d_10000 = int(cc[10000])
    d_100000 = int(cc[100000])
    d_1000000 = int(cc[1000000])

    total = d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

    print(total)


def main():
    p40()


if __name__ == '__main__':
    main()

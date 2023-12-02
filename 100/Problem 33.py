'''
Digit Cancelling Fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathemathician in attemption to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained b cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the products of these four fractions is given in its lowest common terms, find the value of the denominator.
'''


from sympy import N


def p33():
    ntf = []
    for i in range(11, 100):
        for j in range(11, 100):
            v = i / j
            if v >= 1 or i % 10 == 0 or j % 10 == 0:
                continue
            i_digits = []
            j_digits = []

            for a in str(i):
                i_digits.append(a)
            for b in str(j):
                j_digits.append(b)

            i_sum = ''
            j_sum = ''

            for x in i_digits:
                if x in j_digits:
                    i_digits.remove(x)
                    j_digits.remove(x)
                    i_sum += i_digits[0]
                    j_sum += j_digits[0]
            if len(i_sum) < 1 or len(j_sum) < 1:
                continue
            if int(i_sum)/int(j_sum) == i / j:
                ntf.append([i, j])
    print(ntf)
    fn = 1
    fd = 1

    for f in ntf:
        fn *= f[0]
        fd *= f[1]

    print(gcd(fn, fd))


def gcd(a, b):
    n = 0
    d = 0

    if b % a == 0:
        n = 1
        d = b // a

    else:
        n = a
        d = b

    return f'{n} / {d}'


def main():
    p33()


if __name__ == '__main__':
    main()

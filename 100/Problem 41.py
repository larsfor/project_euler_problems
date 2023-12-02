'''
Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import sympy


def p41():
    max_p = 0
    for p in range(3, 7652414, 2):
        # digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        digits = [str(c) for c in range(1, len(str(p))+1)]
        # print(digits)
        if sympy.isprime(p):
            # print(p)
            strp = [c for c in str(p)]
            # print(strp)
            if sorted(strp) == digits and p > max_p:
                print(p)
                print(strp)
                max_p = p
    print(max_p)


def main():
    p41()


if __name__ == '__main__':
    main()

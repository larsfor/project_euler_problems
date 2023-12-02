'''
Factorial Digit Sum

n! means n * (n - 1) * ... * 3 * 2 * 1.
For example, 10! = 10 * 9 * ...* 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

Find the sum of the digits in the number 100!.
'''


def p20(fact):
    f = 1
    for d in range(1, fact+1):
        f *= d

    print(sum([int(x) for x in str(f)]))


def main():
    fact = 100
    p20(fact)


if __name__ == '__main__':
    main()

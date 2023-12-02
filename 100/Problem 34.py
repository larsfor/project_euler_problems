'''
Digit Factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''


def p34():
    total = 0
    for n in range(3, 99999):
        f_sum = 0
        for i in str(n):
            # print(i)
            f_sum += factorial(int(i))
        if n == f_sum:
            # print("found something")
            # print(n)
            total += n
    print(total)


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return factorial(n-1) * n


def main():
    p34()


if __name__ == '__main__':
    main()

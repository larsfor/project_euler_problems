'''
Digit Fifth Powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

                            1634 = 1^4 + 6^4 + 3^4 + 4^4
                            8208 = 8^4 + 2^4 + 0^4 + 8^4
                            9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316
Find the sum of all the numbers that can be written as the sum of fith powers of their digits.
'''


def p30(p):
    symmetrical = []
    for i in range(2, 1000000):
        d = str(i).zfill(6)
        first, second, third, fourth, fifth, sixth = int(
            d[0]), int(d[1]), int(d[2]), int(d[3]), int(d[4]), int(d[5])

        if i == (first**p + second**p + third**p + fourth**p + fifth**p + sixth**p):
            symmetrical.append(i)
    print(sum(symmetrical))


def main():
    powers = 5
    p30(powers)


if __name__ == '__main__':
    main()

'''
Double-base Palindromes

The decimal number, 585 = 1001001001(2), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and 2.
(Please note that the palindromic number, in either base, may noe include leading zeroes):
'''


def p36():
    # d = 585
    pn = []
    for d in range(1_000_001):
        b = convert_to_binary(d)

        if str(d) == str(d)[::-1] and str(b) == str(b)[::-1]:
            pn.append(d)

    print(sum(pn))


def convert_to_binary(d):
    if d < 0:
        return

    bin_len = 0
    while True:
        if 2**bin_len > d:
            break
        bin_len += 1
    binary = []
    temp_decimal = d

    for b in range(bin_len-1, -1, -1):
        if temp_decimal - 2**b >= 0:
            binary.append('1')
            temp_decimal -= 2**b
        else:
            binary.append('0')

    return "".join(binary)


def main():
    p36()


if __name__ == '__main__':
    main()

'''
Take the number 192 and multiply it by each of 1, 2 and 3:
                                        192 x 1 = 192
                                        192 x 2 = 384
                                        192 x 3 = 576

By concatenating each product we got the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1, 2, 3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4 and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1, 2, 3, 4 5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated prodict of an integer with (1, 2,..., n) where n > 1?
'''


def p38():
    n = 1
    prev_max = 918273645
    while True:
        pd, total = concatenate_product(n)

        if pd and prev_max < total:
            prev_max = total
            print(prev_max)

        n += 1
        if n == 9999:
            break


def concatenate_product(n):
    count = 1
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    parts = []
    while True:
        a = str(count * n)
        parts += [x for x in a]
        count += 1
        if len(parts) > 9:
            return False, 0
        if len(parts) == 9:
            break
    return sorted(parts) == digits, int("".join(parts))


def main():
    p38()


if __name__ == '__main__':
    main()

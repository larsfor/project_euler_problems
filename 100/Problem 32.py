'''
Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 in unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can we written as a 1 through 9 pandigital.

HINT: Some products can be obtained in a more than one way, so be sure to only include it once in your sum.
'''


from sympy import O


def p32():
    combinations = []
    pSum = 0
    tries = set()
    for i in range(1, 9999):
        for j in range(1, 9999):
            if i * j > 9999:
                continue
            tries.add((i, j))

            if (j, i) in tries:
                continue

            # print("before", i, j)
            combs = find_combinations(i, j)
            # if combs != False:
            #     print(combs)
            if combs and combs[0][2] not in combinations:
                combinations.append(combs[0][2])
    print(combinations)
    print(sum(combinations))


def find_combinations(i, j):

    combinations = []
    for k in range(9999):
        if i * j != k:
            continue
        digits = []
        possibilities = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for a in str(i):
            digits.append(a)
        for b in str(j):
            digits.append(b)
        for c in str(k):
            digits.append(c)

        if len(digits) > 9:
            return False

        if all([x in digits for x in possibilities]):
            print([i, j, k])
            combinations.append([i, j, k])

    if len(combinations) == 0:
        return False

    return combinations


def main():
    p32()


if __name__ == '__main__':
    main()

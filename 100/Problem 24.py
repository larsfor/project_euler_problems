'''
Lexicographic Permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutations of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
                            012 021 102 120 201 210

What is the millionth lexicographic permutations of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''


from itertools import permutations


def p24(digits):
    ar = getPermutations(digits)
    print(ar)
    # print(ar)
    # a = sorted(list(a))
    # print(a[999999])


arrs = []


def getPermutations(array):
    # from https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list
    if len(array) == 1:
        return [array]
    permutations = []
    for i in range(len(array)):
        perms = getPermutations(array[:i] + array[i+1:])
        for p in perms:
            permutations.append([array[i], *p])
    return permutations


def main():
    # digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # digits = [0, 1, 2]
    digits = [0, 1, 2, 3]
    p24(digits)


if __name__ == '__main__':
    main()

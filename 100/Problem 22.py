'''
Names Scores

Using 22_names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 imes 53 = 49714.
What is the total of all the name scores in the file?
'''


def p22(f):
    names = f.read().split()
    names = names[0].split('"')
    lst = []
    for name in names:
        if len(name) < 2:
            continue
        lst.append(name)
    namesSorted = sorted(lst)

    namesDict = {}
    totalScore = 0
    for index, name in enumerate(namesSorted):
        namesDict[name] = index + 1

    for key, value in namesDict.items():
        totalScore += findScore(key, value)
        # break

    print(totalScore)


def findScore(name, rank):
    alpha = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
             "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

    score = 0
    for c in name:
        score += alpha[c]

    score *= rank

    return score


def main():
    with open("p22names.txt") as f:
        p22(f)


if __name__ == '__main__':
    main()

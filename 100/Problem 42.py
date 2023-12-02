'''
Coded Triangle Numbers

The nth term of the sequence of triangle numbers is given by, tn = 1/2*n*(n+1); so the first ten triangle numbers are:
                                                    1, 3, 6, 10, 15, 21, 28, 36, 45, 55

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word value is a triangle number then we sall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''


def p41(words):
    tNums = [int((1/2*n*(n+1))) for n in range(1, 100)]
    count = 0
    for word in words:
        num = sum(find_word_values(word))
        if num in tNums:
            count += 1
    print(count)


def find_word_values(w):
    return [ord(c)-64 for c in w]


def main():
    with open('p42_words.txt') as f:
        words = f.read().replace('"', "").split(",")
        p41(words)


if __name__ == '__main__':
    main()

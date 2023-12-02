'''
Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three four, five, then there are 3+3+5+4+4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in worsd, how many letter would be used?

NOTE: Do not count space or hyphens. For example, 342 (three hundred and forty-two) contains 23 letter and 115 (one hunded and fifteen) contains 20 letter. THe use of "and" when writing out numbers is in copliance with British usage.
'''
from num2words import num2words

def p17(number):
    wordLen = 0
    for i in range(1, number+1):
        n = num2words(i).replace("-", "").split()
        l = len("".join(n))
        wordLen += l
    print(wordLen)


if __name__ == '__main__':
    p17(1000)
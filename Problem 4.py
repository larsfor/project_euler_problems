'''
Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def p4():
    palindrome = 0
    nums = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if str(num) == str(num)[::-1] and num > palindrome:
                nums = []
                nums.append([i, j])
                palindrome = num
    print(palindrome, nums)


if __name__ == '__main__':
    p4()
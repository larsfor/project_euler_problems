'''
10_001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can se that the 6th prime is 13.
What is the 10 001st prime number
'''

import math


def p7(n):
    numbers = [2]
    num = 3
    while True:
        # if hasPrimeFactor(num):
            # numbers.append(num)            
        # if  hasPrimeFactorSieve(n):
        #     numbers.append(n)            

        # Solution from https://codereview.stackexchange.com/questions/102507/finding-the-10001st-prime
        if all(num % number != 0 for number in numbers):
            numbers.append(num)
        num += 2
        if len(numbers) >= n:
            # print(numbers)
            print(numbers[-1])
            break


def hasPrimeFactor(n):
    # solution retrieved from https://www.youtube.com/watch?v=ZAXBboNypJ4 
    # modified to oblivion by me
    i = 2
    p = n
    nums = []
    isPrime = True
    while(n != 1):
        rem = n % i
        if (rem == 0):
            n /= i
            nums.append(i)
        else:
            i += 1 
    for i in nums:
        if i not in [1, p]:
            isPrime = False
            break
    return isPrime


def hasPrimeFactorSieve(num):
    p_n = int(2 * num * math.log(num)) # over-estimate number of p_ns https://codereview.stackexchange.com/questions/102507/finding-the-10001st-prime

    sieve = [True] * p_n
    count = 0

    for i in range(2, p_n):
        if sieve[i]:
            count += 1
            if count == num:
                return i
            for j in range(2*i, p_n, i):
                sieve[j] = False

if __name__ == '__main__':
    p7(10_001) # 104 743
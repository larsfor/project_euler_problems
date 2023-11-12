'''
10_001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can se that the 6th prime is 13.
What is the 10 001st prime number
'''

def p7(n):
    numbers = []
    num = 3
    while True:
        if hasPrimeFactor(num):
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


if __name__ == '__main__':
    p7(10_001) # 104 743
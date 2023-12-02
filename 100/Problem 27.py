'''
Quadratic Primes

Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0  n  39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0  n  79. The product of the coefficients, -79 and 1601, is -126479.
Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| <= 1000 where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

# import sympy
import math


def p27():
    ip_best = 0
    a_best = 0
    b_best = 0
    for a in range(-999, 1000):
        for b in range(1, 1001, 2):
            n = 0
            while is_prime((n**2 + a*n + b)):
                n += 1
            if n > ip_best:
                ip_best = n
                a_best = a
                b_best = b

    print("ip_best", ip_best, "a_best:", a_best,
          "b_best:", b_best)


def quadratic3(n, a, b):
    return n**2 + a*n + b


def is_prime(n):
    # Take the number
    # If the number is 2 then it is a Prime number else follow the next steps
    # Derive the square root of the number
    # Take the upper bound of the square root obtained and then minus it by one
    # Divide the number with all the numbers between 2 and the square root of the number
    # If the remainder is 0 in any of the divisions then non-prime.
    # Else it is the prime number
    if n < 2:
        return False
    if n == 2:
        return True
    upper_bound = math.ceil(n**0.5) + 1
    for i in range(2, upper_bound):
        if n % i == 0:
            return False
    return True


def main():
    p27()


if __name__ == '__main__':
    main()

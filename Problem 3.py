'''
Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 
'''

def p3(n):
    # solution retrieved from https://www.youtube.com/watch?v=ZAXBboNypJ4 
    i = 2
    while(n != 1):
        rem = n % i
        if (rem == 0):
            n /= i
            print(i)
        else:
            i += 1 
    # pss = is_prime_sieve(ps)
    # pfs = find_prime_factors(pss, ps)

# def is_prime_sieve(number):
#     numbers = []

#     for i in range(2, number+1):
#         numbers.append(i)
#         if len(numbers) > 1000:
#             break

#     for i in numbers:
#         for j in range(i, number+1, i):
#             if i == j:
#                 continue
#             if j in numbers:
#                 numbers.remove(j)
#     return numbers

# def find_prime_factors(pss, ps):
#     sett = set()
#     rest = ps
#     for i in pss:
#         while True:
#             if rest % i == 0:
#                 rest /= i
#                 sett.add(i)
#             if rest % i != 0:
#                 break
#         if rest == 1:
#             break
#     print(sorted(sett)) 


if __name__ == '__main__':
    p3(600851475143)
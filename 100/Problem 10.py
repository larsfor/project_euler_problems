'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all the primes below two million.
'''

# With a lot of help from https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def p10(limit):
    sieve = [True for x in range(limit)]
    for i in range(2, int(limit**0.5)+1):
        if sieve[i-2]:
            for j in range(i, limit+2, i):
                # print("i", i, "j", j)
                if j == i:
                    continue 
                # print("removing", j)
                sieve[j-2] = False

    # print(sieve)

    primes = []
    count = 2
    for i in range(len(sieve)-2):
        if sieve[i]:
            primes.append(count)
        count += 1

    # print(primes)
    print(sum(primes))




if __name__ == '__main__':
    p10(2_000_000)
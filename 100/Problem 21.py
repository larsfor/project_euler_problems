'''
Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a e b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''


def p21():
    pds = {}
    pairs = []
    start = 1
    end = 10_000
    # end = 285

    for i in range(start, end):
        pd = find_pd(i)
        if pd in [0, 1, i]:
            continue
        pds[i] = pd

    for key, value in pds.items():
        for comp in range(end):
            try:
                if key == pds[comp] and comp == value:
                    # pairs.append([key, comp])
                    pairs.append(key)
            except:
                continue

    print(pairs)
    print(sum(pairs))
    # print(pds)


def find_pd(n):
    ds = []
    for i in range(1, n):
        if n % i == 0:
            ds.append(i)
    # print(ds)
    return sum(ds)


def main():
    p21()


if __name__ == '__main__':
    main()

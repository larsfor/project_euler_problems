'''
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
                                                            a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which a + b + c = 1 000.
Find the product abc
'''

def p9():
    a, b, c = 1, 1, 1

    for x in range(999):
        for y in range(999):
            for z in range(999):
                c += 1
                if c > 999:
                    c = 0
                    b += 1
                if b > 999:
                    b = 0
                    a += 1
                # print("a", a, "b", b, "c", c)
                
                if a + b + c == 1000 and (a**2 + b**2) == c**2:
                    print("found it")
                    print("a", a, "b", b, "c", c)
                    print("product", a*b*c)
                    return
                
                if a == b == c == 999:
                    return


if __name__ == '__main__':
    p9() 
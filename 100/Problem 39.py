'''
Integer Right Triangles

If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p = 120.

{20, 48, 52}, {24, 45, 51}, {30, 40, 50}

For which value of p<=1000, is the number of solutions maximized?
'''


def p39():
    max_solutions = 0
    max_p = 0

    for p in range(1, 1001):
        a = calculate(p)
        if len(a) > max_solutions:
            max_solutions = len(a)
            max_p = p
    print("max p", max_p, "max solutions", max_solutions)


def calculate(p):
    solutions = []
    for a in range(1, p+1):
        for b in range(1, p+1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                if sorted([a, b, c]) not in solutions:
                    solutions.append([a, b, c])
    return solutions


def main():
    p39()


if __name__ == '__main__':
    main()

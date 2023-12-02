'''
1000-digit Fibonacci Number

The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn-1 + Fn-2, where F1 = and F2 = 1

Hence the first 12 terms will be: 

F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, F7 = 13 F8 = 21, F9 = 34, F10 = 55, F11 = 89, F12 = 144,

The 12th term, F12 is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''


def p25():
    terms = 1

    while True:
        a = getFib(terms)
        # print(a, len(str(a)))

        if len(str(a)) == 1000:
            print("1000 digits", terms)
            break

        terms += 1


def getFib(terms):
    return fibonacci(terms)


def fibonacci(term, computed={0: 0, 1: 1}):
    # Memoization inspired from https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
    if term not in computed:
        computed[term] = fibonacci(term-1, computed) + \
            fibonacci(term-2, computed)

    return computed[term]


def main():
    p25()


if __name__ == '__main__':
    main()

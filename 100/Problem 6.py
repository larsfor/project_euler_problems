'''
Sum Square Differences

The sum of the squares of the first ten natural numbers is 1^2 + 2^2 ...+10^2 = 385
The square of the sum of the first ten natural numbers is (1+2+...+10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hunded natural numbers and the square of the sum.
'''

def p6(n):
    sumOfSquare = 0
    squareOfSum = 0
    
    for i in range(1, n+1):
        sumOfSquare += i**2
        squareOfSum += i
    
    difference = squareOfSum**2 - sumOfSquare
    print(difference)


if __name__ == '__main__':
    p6(100)
'''
Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that evenly divisible by all of the numbers from 1 to 20?
'''

def p5(num):
    n = num
    while True:
        divisile = []
        # print(n)
        for i in range(1, num+1):
            if n % i != 0:
                break
            divisile.append(i)
        # print(divisile)
        if len(divisile) == num:
            print(n)
            break
        n += num




if __name__ == '__main__':
    p5(20)
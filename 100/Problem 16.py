'''
Power Digit Sum

2^15 = 32768 and the sum of its digits is 3+2+7+6+8 = 26.
What is the sum of the digits of the number 2^1000?
'''

def p16(ex):
    sum = 0
    e = str(2**ex)
    for d in e:
        sum += int(d)    
    print(sum)



if __name__ == '__main__':
    p16(1000)
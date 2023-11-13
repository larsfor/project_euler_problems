'''
Largest Product in a Series

The four adjecent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5382
Find the thirteen adjecent digits in the 1000-digit number that have the greatest product. What is the value of this product.
'''

def p8(digits):
    separated = [x for x in digits if x != '\n']
    start = 0
    end = 13
    pMax = 0 
    bestProd = []

    while True:
        product = separated[start:end]
        if product == ["0","4","2","0","7","5","2","9","6","3","4","5","0"]:
            break
        sumProduct = sumProd(product) 
        # print(sumProduct)
        if pMax < sumProduct:
            pMax = sumProduct 
            bestProd = product
        start += 1
        end += 1
    print("product", bestProd)
    print("pMax", pMax)
    

def sumProd(numbers):
    if '0' in numbers:
        return 0
    prod = 1
    for n in numbers:
        prod *= int(n)
    return prod

if __name__ == '__main__':
    with open("p8text.txt") as f:
        digits = f.read()
        p8(digits) 
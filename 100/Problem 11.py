'''
In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.
            " 20 x 20 grid"
The product of these numbers is 26 * 63 * 78 * 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right or diagonally) in the 20x20 grid?
'''

def p11(digits):
    # Adding the digits to a list as int and without linebreak
    fixedDigits = []
    grid = []
    row = []
    for line in digits:
        fixedDigits.append(line.split(" "))
    
    for line in fixedDigits:
        for num in line:
            row.append(int(num))
        grid.append(row)
        row = []

    pMax = 0
    cell = []

    # Looping through the grid checking for each possibility and their respective product
    # Row
    for i in range(20):
        # Column
        for j in range(20):
            product = searchProduct([i, j], grid)
            if product > pMax:
                cell = []
                cell.append([i, j])
                pMax = product
    print(pMax, cell)



def searchProduct(cell, grid):
    i, j = cell
    product = 0
    combinations = [
        # i  j      i  j    i   j     i  j
        [[0, 0],  [-1,  0], [-2,  0], [-3,  0]], # straight up
        [[0, 0],  [-1,  1], [-2,  2], [-3,  3]], # diagonally up right
        [[0, 0],  [ 0,  1], [ 0,  2], [ 0,  3]], # straight right
        [[0, 0],  [ 1,  1], [ 2,  2], [ 3,  3]], # diagonally down right
        [[0, 0],  [ 1,  0], [ 2,  0], [ 3,  0]], # straight down
        [[0, 0],  [ 1, -1], [ 2, -2], [ 3, -3]], # diagonally down left
        [[0, 0],  [ 0, -1], [ 0, -2], [ 0, -3]], # straight left
        [[0, 0],  [-1, -1], [-2, -2], [-3, -3]], # diagonally up left
    ]

    for row in combinations:
        partProduct = 1
        for col in row:
            x_i, x_j = col
            if i + x_i < 0 or j + x_j < 0:
                continue
            try:
                value = grid[i + x_i][j + x_j]
            except:
                continue
            partProduct *= value
        if partProduct > product:
            product = partProduct 
    
    # print(product)


    return product


if __name__ == '__main__':
    with open('p11text.txt') as f:
        digits = f.read().splitlines()
        p11(digits) # 70 600 674 (12, 6)
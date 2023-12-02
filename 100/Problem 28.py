'''
Number Spiral Diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formes as follows:

                                            [21]  22  23  24  [25]
                                             20   [7]  8  [9]  10
                                             19    6  [1]  2   11
                                             18   [5]  4  [3]  12
                                            [17]  16  15  14  [13]

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed the same way? 
'''


from turtle import left


def p28(s):
    # Creating an [s x s] grid
    grid = [[0 for _ in range(s)] for _ in range(s)]
    grid = populate_grid(grid, s)
    sumDiag = sum_diagonals(grid, s)

    print(sumDiag)


def populate_grid(grid, s):
    mid = s // 2
    row, col = mid, mid
    dirs = ["r", "d", "l", "u"]
    dd = {
        "r": [0,  1],
        "d": [1,  0],
        "l": [0,  -1],
        "u": [-1, 0]
    }

    count = 0
    shift = 1
    num = 1

    for _ in range(1, s*2):
        d = dirs[0]
        for _ in range(shift):
            grid[row][col] = num
            row += dd[d][0]
            col += dd[d][1]
            num += 1
        count += 1

        if count == 2:
            shift += 1
            count = 0
        dirs.append(dirs.pop(0))
    return grid


def sum_diagonals(grid, s):
    left_down = []
    right_down = []
    dSum = 0
    c = s-1
    mid = s // 2

    for i in range(s):
        left_down.append([i, i])
        right_down.append([c, i])
        c -= 1

    # Subtracting the mid because it's summed twice
    dSum -= grid[mid][mid]

    # Go through the cells diagonally and add the cell values to dSum
    for i in range(s):
        li, lj = left_down[i]
        dSum += grid[li][lj]

        ri, rj = right_down[i]
        dSum += grid[ri][rj]

    return dSum


def main():
    sGrid = 1001
    p28(sGrid)


if __name__ == '__main__':
    main()

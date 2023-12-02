'''
Maimum Path Sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

                                    [3]
                                   [7] 4
                                  2 [4] 6
                                 8 5 [9] 3

'''


def p18(triangle):
    t = [x.split() for x in triangle.splitlines()]
    t = [[int(x) for x in lst]for lst in t]
    print(max_path_sum(t))

    # tr = Tree(triangle)
    # tr.print_tree()
    # p = tr.findMaxSum()
    # print(p)
    # print(tr.routes())


def max_path_sum(triangle):
    # The idea is to start from the bottom of the triangle and work your way up, computing the maximum sum at each level.
    n = len(triangle)

    # Initialize a new 2D array with the same dimensions as the original triangle.
    dp = [[0] * n for _ in range(n)]

    # Copy the last row of the original triangle to the new array.
    dp[-1] = triangle[-1]

    # Starting from the second-last row of the original triangle, compute the maximum sum for each element
    # in that row by adding the element to the maximum of its two children in the new array.
    # Repeat for all rows until you reach the top of the triangle.
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = triangle[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])
            print(dp)

    # The maximum sum will be the first element in the new array.
    return dp[0][0]

# class Node:
#     def __init__(self, value) -> None:
#         self.value = value
#         self.left = None
#         self.right = None


# class Tree:
#     def __init__(self, array) -> None:
#         self.array = array
#         self.tree = self.build_tree(array)
#         self.queue = []

#     def root(self):
#         return self.tree[0]

#     def findMaxSum(self):
#         maxSum = 0
#         route = []
#         root = self.root()

#         combos = itertools.combinations_with_replacement(
#             ["left", "right"], self.routes())

#         root = self.root()
#         for r in combos:
#             curSum = 0
#             curRoute = []
#             for d in r:
#                 if root == None:
#                     continue
#                 curSum += root.value
#                 curRoute.append(root.value)
#                 if d == "left":
#                     root = root.left
#                 elif d == "right":
#                     root = root.right
#             root = self.root()
#             if curSum > maxSum:
#                 route = curRoute
#                 maxSum = curSum
#             curSum = 0
#             curRoute = []

#         return maxSum, route

#     def build_tree(self, array):
#         t = [Node(int(x)) for x in array.split()]
#         rl = 1
#         i = 0
#         for id, n in enumerate(t):
#             try:
#                 n.left = t[id+rl]
#                 n.right = t[id+rl+1]
#                 if i+1 == rl:
#                     i = 0
#                     rl += 1
#                     continue
#                 i += 1
#             except:
#                 continue
#         return t

#     def print_tree(self):
#         for n in self.tree:
#             print("value", n.value, "left", n.left, "right", n.right)

#     def height(self):
#         return len(self.array.splitlines())

#     def routes(self):
#         # Find the number of routes based on Pascal's Triangle
#         row = [1]
#         for i in range(self.height()):
#             row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
#         return sum(row)//2


def main():
    # triangle = '''75
    # 95 64
    # 17 47 82
    # 18 35 87 10
    # 20 04 82 47 65
    # 19 01 23 75 03 34
    # 88 02 77 73 07 63 67
    # 99 65 04 28 06 16 70 92
    # 41 41 26 56 83 40 80 70 33
    # 41 48 72 33 47 32 37 16 94 29
    # 53 71 44 65 25 43 91 52 97 51 14
    # 70 11 33 28 77 73 17 78 39 68 17 57
    # 91 71 52 38 17 14 91 43 58 50 27 29 48
    # 63 66 04 68 89 53 67 30 73 16 69 87 40 31
    # 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
    triangle = '''3
    7 4
    2 4 6
    8 5 9 3'''

    p18(triangle)


if __name__ == '__main__':
    main()

'''
Largest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
                                    13->40->20->10->5->16->8->4->2->1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not yet been 
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under on mission, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def p14(n):
    longest = 0
    longest_n = n
    while n < 1_000_000:
        # print(n)
        length = CollatzLen(n)
        if length > longest:
            longest = length
            longest_n = n
        n += 1
    print(longest, longest_n)
        
       
def CollatzLen(n):
    t = n
    count = 1
    while True:
        # print(t)
        if t % 2 == 0:
            t = t/2
        else:
            t = 3*t + 1
        count += 1

        if t == 1:
            return count


if __name__ == '__main__':
    p14(13)
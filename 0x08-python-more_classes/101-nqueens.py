#!/usr/bin/python3
"""A program that solves the N queens puzzle"""


def nqueens(argv):
    """A function that solves the nqueens puzzle
        arguments:
            argv: list arguments recieved from the command line
        Returns: nothing
    """
    if (len(argv) != 2):
        print("Usage: nqueens N")
        exit(1)
    N = int(argv[1])
    if not isinstance(N, int):
        print("N must be a number")
        exit(1)
    if (N < 4):
        print("N must be at least 4")
        exit(1)

    nqlist = []
    nqlist3 = []

    for i in range(N):
        for j in range(N):
            if (j == i):
                continue
            if (j + i == N - 1):
                continue
            nqlist.insert(0, [i, j])

    nqlist.sort()
    for i in nqlist:
        i.reverse()
    num = int((len(nqlist))/N)

    k = 0 - N
    lst = 0

    for i in range(num):
        k = k + N
        lst = lst + N
        nqlist3.insert(0, nqlist[k:lst])

    nqlist3.sort()
    for i in nqlist3:
        i.sort()
        print(i)


if __name__ == "__main__":
    import sys
    nqueens(sys.argv)

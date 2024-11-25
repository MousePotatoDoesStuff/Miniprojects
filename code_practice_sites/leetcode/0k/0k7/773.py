from collections import deque
from typing import *
import inspect


def puzzleToInt(board):
    L = board[0] + board[1]
    res = L.index(0)
    while L:
        res <<= 3
        res |= L.pop()
    return res


def intToPuzzle(n):
    E = []
    for i in range(6):
        n, cur = divmod(n, 8)
        E.append(cur)
    return [n, E[:3], E[3:]]


MAINMASK = (1 << 18) - 1


def swap(n, a, b):
    n |= a << 18
    a *= 3
    b *= 3
    mask = n & (7 << a)
    n ^= mask
    add = (mask >> a) << b
    n |= add
    return n


NEIGH = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]


def getNeigh(n):
    cur = n >> 18
    n &= MAINMASK
    res = []
    for e in NEIGH[cur]:
        nex = swap(n, e, cur)
        res.append(nex)
    return res


SOLVED = puzzleToInt([[1, 2, 3], [4, 5, 0]])


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = puzzleToInt(board)
        used = set()
        nex = deque([(board, 0)])
        while nex:
            board, count = nex.popleft()
            if board in used:
                continue
            if board == SOLVED:
                return count
            count += 1
            used.add(board)
            for e in getNeigh(board):
                if e in used:
                    continue
                nex.append((e, count))
        return -1

    main = slidingPuzzle


TESTS = [
    (
        ([[1, 2, 3], [4, 0, 5]],),
        "test")
    ,
    (
        ([[1, 2, 3], [5, 4, 0]],),
        "also test"
    )
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    print("Running...")
    for i, (args, true_res) in enumerate(tests):
        res = SOL.main(*args)
        count += res == true_res
        if only_show_errors and res == true_res:
            continue
        print(f"Test {i + 1}")
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))
    print(f"{count} out of {len(tests)} tests passed")


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()

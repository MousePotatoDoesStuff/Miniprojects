from collections import deque
from typing import *
import inspect


class Solution:
    def __init__(self):
        self.delcount = 0
        self.n = 0
        self.m = 0
        self.grid = None
        self.nexts = None
        self.currents = None

    def getNext(self, i, j):
        RES=([],[])
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ci, cj = i + di, j + dj
            if ci not in range(self.n):
                continue
            if cj not in range(self.m):
                continue
            v=self.grid[ci][cj]
            if v & 2:
                continue
            RES[v].append((ci, cj))
            self.grid[ci][cj] |= 2
        return RES

    def step(self):
        i, j = self.currents.pop()
        if i==self.n-1 and j==self.m-1:
            return True
        v = self.grid[i][j]
        nexlist:deque = [self.currents, self.nexts][v & 1]
        neigh_empty,neigh_full = self.getNext(i, j)
        nexlist.extend(neigh_empty)
        nexlist.extendleft(neigh_full)
        return False

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        self.grid[0][0] = 2
        self.currents = deque([(0, 0)])
        self.nexts = deque()
        self.delcount = 0

        while not self.step():
            if self.currents:
                continue
            self.currents = self.nexts
            self.nexts = deque()
            self.delcount += 1

        return self.delcount

    main = minimumObstacles


TESTS = [
    (
        ([[0, 1, 1], [1, 1, 0], [1, 1, 0]],),
        2
    )
    ,
    (
        ([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]],),
        0
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

import heapq
from collections import defaultdict
from typing import *
import inspect


class Solution:
    def __init__(self):
        self.grid = [[0]]
        self.END=0,0

    def addEl(self, i, j, v):
        if v in self.PQD:
            self.PQD[v].add((i, j))
        else:
            heapq.heappush(self.PQ, v)
            self.PQD[v] = {(i, j)}
        self.grid[i][j] = ~v

    def getNext(self, i, j, nextime):
        offset = ((i + j) & 1) ^ 1
        X=[]
        if i>0:
            X.append((i-1,j))
        if i<self.END[0]:
            X.append((i+1,j))
        if j>0:
            X.append((i,j-1))
        if j<self.END[1]:
            X.append((i,j+1))
        for nex_i, nex_j in X:
            minimum = self.grid[nex_i][nex_j]
            if minimum < 0:
                continue
            if minimum < nextime:
                minimum = nextime
            elif minimum & 1 != offset:
                minimum += 1

            self.addEl(nex_i, nex_j, minimum)
        return

    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        self.grid = grid
        self.PQ: list[int] = []
        self.PQD = {}
        self.addEl(0, 0, 0)
        self.END = len(self.grid)-1,len(self.grid[0])-1
        while self.PQ:
            curtime = heapq.heappop(self.PQ)
            curvals = self.PQD.pop(curtime)
            for E in curvals:
                if E == self.END:
                    return curtime
                self.getNext(*E, curtime + 1)
        return -1

    main = minimumTime


TESTS = [
    (
        ([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]],),
        7)
    ,
    (
        ([[0, 7], [7, 2]],),
        -1
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

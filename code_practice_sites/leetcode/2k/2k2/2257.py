from typing import *
import inspect


def markRowsAndCols(cells: list, row_lim: int, col_lim: int):
    cells.sort(key=tuple)
    byRow = dict()
    byCol = dict()
    while cells:
        r, c = cells.pop()
        byRow.setdefault(r, [col_lim]).append(c)
        byCol.setdefault(c, [row_lim]).append(r)
    return byRow, byCol


def getUnguardedRanges(guards: list[int], walls: list[int]):
    unguardedRanges = []
    lastUnguarded = 0
    while walls:
        nexWall = walls.pop()
        free=True
        while guards and guards[-1] < nexWall:
            free=False
            guards.pop()
        if free:
            unguardedRanges.append((lastUnguarded, nexWall))
        lastUnguarded = nexWall + 1
    return unguardedRanges


def getUnguarded(guardsBy: dict[int, list[int]], wallsBy: dict[int, list[int]], mn: int):
    indices = set(guardsBy) | set(wallsBy)
    unguarded_res = dict()
    for ind in indices:
        guards = guardsBy.get(ind, [mn + 1])
        walls = wallsBy.get(ind, [mn])
        unguarded = getUnguardedRanges(guards, walls)
        unguarded_res[ind] = unguarded
    return unguarded_res


def findUnguarded(byRow: dict[int, list], byCol: dict[int, list], row_lim: int, col_lim: int):
    curCols = {e: 0 for e in byCol}
    for E in byCol.values():
        E.append((row_lim, row_lim))
    res = 0
    for i in range(row_lim):
        row = byRow.get(i, [(0, col_lim)])
        for start, end in row:
            for j in range(start, end):
                if j not in curCols:
                    res += 1
                    continue
                cur = curCols[j]
                C = byCol[j]
                while C[cur][1] <= i:
                    cur += 1
                curCols[j] = cur
                if C[cur][0] <= i:
                    res += 1
    return res


class Solution:
    def countUnguarded(self, row_limit: int, col_limit: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guardsByRow, guardsByCol = markRowsAndCols(guards, row_limit+1, col_limit+1)
        wallsByRow, wallsByCol = markRowsAndCols(walls, row_limit, col_limit)
        unguardedByRow = getUnguarded(guardsByRow, wallsByRow, col_limit)
        unguardedByCol = getUnguarded(guardsByCol, wallsByCol, row_limit)
        unguardedCount=findUnguarded(unguardedByRow,unguardedByCol,row_limit,col_limit)
        return unguardedCount

    main = countUnguarded


TESTS = [
    (
        (
            4, 6,
            [[0, 0], [1, 1], [2, 3]],
            [[0, 1], [2, 2], [1, 4]]
        ),
        7)
    ,

    (
        (
            4, 3,
            [[1, 0]],
            [[0,0],[1,2],[0,2],[2,1],[0,1],[2,2]]
        ),
        2)
    ,

    (
        (
            9,6,
            [[8, 2]],
            [[2,3],[2,4],[6,5],[2,0],[5,3],[7,5],[4,2],[3,0]]
        ),
        37)
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
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

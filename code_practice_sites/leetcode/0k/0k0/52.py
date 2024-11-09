from collections import defaultdict
from typing import *
import inspect


def stepOne(left: int, mid: int, right: int, mask: int):
    left <<= 1
    left &= mask
    right >>= 1
    options = left | mid | right
    cur = 1
    res = []
    while cur & mask:
        if not options & cur:
            E = left | cur, mid | cur, right | cur
            res.append(E)
        cur<<=1
    return res


def stepBulk(allSols: defaultdict, mask: int):
    nexSols = defaultdict(int)
    for e, v in allSols.items():
        L = stepOne(*e,mask=mask)
        for el in L:
            nexSols[el] += v
    return nexSols


class Solution:
    def totalNQueens(self, n: int) -> int:
        sols = {(0, 0, 0): 1}
        mask = 1 << n
        mask -= 1
        for _ in range(n):
            sols = stepBulk(sols, mask)
        return sum(sols.values())

    main = totalNQueens


TESTS = [
    (
        ([0, 1], 1),
        "test")
    ,
    (
        ([0, 1], 2),
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
    return


if __name__ == "__main__":
    main()

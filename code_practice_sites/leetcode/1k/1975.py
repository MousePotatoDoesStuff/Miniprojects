from typing import *
import inspect


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        passed = [0, -float('inf')]
        while matrix:
            neg = 0
            E = matrix.pop()
            lowest = abs(E[0])
            best = 0
            while E:
                cur = E.pop()
                if cur < 0:
                    neg ^= 1
                    cur = -cur
                best += cur
                if lowest>cur:
                    lowest=cur
            nex = [0, 0]
            for i in range(2):
                nex[i ^ neg] = max(passed[i], passed[i ^ 1] - (lowest << 1)) + best
            passed = nex
        return passed[0]

    main = maxMatrixSum


TESTS = [
    (
        ([[1, -1], [-1, 1]],),
        4
    )
    ,
    (
        ([[1, 2, 3], [-1, -2, -3], [1, 2, 3]],),
        16
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

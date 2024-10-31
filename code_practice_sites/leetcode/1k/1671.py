from typing import *
import inspect

from sympy import false


def minLeft(L: list):
    C = [-1]
    res: list = []
    for i, e in enumerate(L):
        N = [1 << 31]
        nexbest = -1
        for nexbest, curmin in enumerate(C):
            if curmin < e:
                break
        else:
            nexbest += 1
        for skipped, curmin in enumerate(C):
            N.append(curmin)
        res.append(nexbest)
        N[nexbest] = min(N[nexbest], e)
        C = N
    return res


def merge_crit(left: list, right: list):
    best = 1 << 32
    count = 0
    while left:
        a = left.pop()
        b = right.pop()
        if a != len(left) and b != count:
            best = min(best, a + b)
        count += 1
    return best


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        left = minLeft(nums)
        nums.reverse()
        right = minLeft(nums)
        right.reverse()
        nums.reverse()
        res = merge_crit(left, right)
        return res

    main = minimumMountainRemovals


TESTS = [
    (
        ([9, 8, 1, 7, 6, 5, 4, 3, 2, 1],),
        2
    ),
    (
        ([100,92,89,77,74,66,64,66,64],),
        6
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
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()

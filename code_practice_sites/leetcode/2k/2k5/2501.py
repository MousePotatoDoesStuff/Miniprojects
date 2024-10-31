from typing import *
import inspect


def numset(L):
    L.sort()
    L2 = [L.pop()]
    while L:
        e = L.pop()
        if e != L2[-1]:
            L2.append(e)
    return L2


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = numset(nums)
        nums.sort(reverse=True)
        recorded = {}
        best = 1
        while nums:
            cur = nums.pop()
            step = 1
            nex = cur * cur
            if cur in recorded:
                cur, add = recorded.pop(cur)
                step += add
            if step > best:
                best = step
            if nex > 100000:
                continue
            recorded[nex] = cur, step
        return best if best > 1 else -1

    main = longestSquareStreak


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
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()

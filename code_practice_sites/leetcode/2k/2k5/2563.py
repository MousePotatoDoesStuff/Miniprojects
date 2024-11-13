from typing import *
import inspect


def sum_less_equal(nums, upper):
    end = len(nums) - 1
    res = 0
    for start, cur in enumerate(nums):
        if cur + nums[0] > upper:
            break
        while cur + nums[end] > upper:
            end -= 1
        if start >= end:
            break
        res += end - start
    return res


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        leq_upper = sum_less_equal(nums, upper)
        lt_lower = sum_less_equal(nums, lower - 1)
        print(leq_upper, lt_lower)
        return leq_upper - lt_lower

    main = countFairPairs


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

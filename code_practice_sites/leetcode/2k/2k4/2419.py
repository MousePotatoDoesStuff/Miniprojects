from typing import *
import inspect


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Finds the longest subarray that has the maximum possible bitwise AND.
        Because the bitwise AND value of two positive numbers will always be smaller than the larger number,
        this subarray will always be the longest subarray consisting solely of the largest number in the array.
        :param nums:
        :return:
        """
        first = -1  # First element of current streak
        largest = max(nums)  # Largest number.
        best = 0  # Current best streak.
        nums.append(-1)
        for i, e in enumerate(nums):
            if e == nums[first]:  # No change.
                continue
            if nums[first] == largest:  # A max streak ends, check result
                best = max(best, i - first)
            first = i  # Current streak ends.
        return best

    main = longestSubarray


TESTS = [
    (
        ([1, 2, 3, 3, 2, 2],),
        2)
    ,
    (
        ([1, 2, 3, 4],),
        1
    )
    ,
    (
        ([100, 5, 5],),
        1
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

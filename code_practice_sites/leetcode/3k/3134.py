from collections import defaultdict
from typing import *


class Solution:
    def checkStep(self, key, target):
        freq = defaultdict(int)
        val = j = 0
        for i, x in enumerate(self.nums):
            freq[x] += 1
            while len(freq) > key:
                freq[self.nums[j]] -= 1
                if freq[self.nums[j]] == 0:
                    freq.pop(self.nums[j])
                j += 1
            val += i - j + 1
        return val < target

    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        self.nums = nums
        n = len(nums)
        target = (n * (n + 1) // 2 + 1) // 2
        lo, hi = 0, n
        while lo < hi:
            mid = lo + hi >> 1
            if self.checkStep(mid, target):
                lo = mid + 1
            else:
                hi = mid
        return lo

    main = medianOfUniquenessArray


def test():
    return ([0, 1], 1), "test"


def main():
    SOL = Solution()
    args, true_res = test()
    res = SOL.main(*args)
    print("Got {} ({})".format(res, type(res)))
    print("Expected {} ({})".format(true_res, type(true_res)))
    return


if __name__ == "__main__":
    main()

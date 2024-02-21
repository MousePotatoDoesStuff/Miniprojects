import random
import time
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self, threshold=10) -> List[int]:
        self.nums.clear()
        L = self.original[:]
        count = len(L)
        null = 1 << 32
        while count > 0:
            for hits in range(threshold):
                i = random.randint(0, len(L) - 1)
                if L[i] is null:
                    continue
                self.nums.append(L[i])
                L[i] = null
                count -= 1
                break
            else:
                L = [e for e in L if e is not None]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


def main():
    S = Solution([i for i in range(40)])
    R = dict()
    best = 1000
    for threshold in range(1, 100):
        a = time.time()
        X = dict()
        for i in range(10000):
            S.shuffle(threshold)
        b = time.time()
        if b - a < best:
            print("BEST BY {}".format(round(1 - (b - a) / best, 3)), end="\t")
            best = b - a
        else:
            print("\t\t\t", end="\t\t\t")
        print(threshold, "->", b - a, X)
    return


if __name__ == "__main__":
    main()

import bisect
from typing import *
import inspect

loggedPrimes = [2, 3, 5, 7]


def nextPrime(n):
    cur = loggedPrimes[-1]
    sqrt = int(cur ** 0.5) + 2
    lim = 3
    while loggedPrimes[-1] < n:
        cur += 2
        if sqrt * sqrt <= cur + 2:
            sqrt += 1
        if loggedPrimes[lim] < sqrt:
            lim += 1
        for i in range(lim):
            if cur % loggedPrimes[i] == 0:
                break
        else:
            loggedPrimes.append(cur)
    return


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        cur = nums.pop()
        while nums:
            last = cur
            cur = nums.pop()
            if cur < last:
                continue
            diff = cur - last + 1
            if diff > loggedPrimes[-1]:
                nextPrime(diff)
            tdiff = loggedPrimes[bisect.bisect_left(loggedPrimes, diff)]
            cur -= tdiff
            if cur <= 0:
                return False
        return True

    main = primeSubOperation


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

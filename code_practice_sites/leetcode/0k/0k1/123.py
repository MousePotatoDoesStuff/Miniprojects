from typing import *
import inspect


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.reverse()
        lowest_first = prices.pop()
        first_res = 0
        lowest_second = lowest_first
        second_res = 0
        while prices:
            cur = prices.pop()
            lowest_first = min(lowest_first, cur)
            lowest_second = min(lowest_second, cur - first_res)
            first_res = max(first_res, cur - lowest_first)
            second_res = max(second_res, cur - lowest_second)
        return second_res

    def maxProfitArray(self, prices: List[int], tries: int = 2) -> int:
        prices.reverse()
        lowest: list[int] = [prices.pop()] * tries
        res: list[int] = [0] * (tries + 1)
        while prices:
            cur = prices.pop()
            i=tries
            for i, e in enumerate(lowest):
                lowest[i] = min(e, cur - res[i])
            for i, e in enumerate(lowest):
                res[i + 1] = max(res[i+1], cur - e)
        return res[-1]

    main = maxProfit


TESTS = [
    [3,2,6,5,0,3] #[3,3,5,0,0,3,1,4]
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    print("Running...")
    for i, L in enumerate(tests):
        res = SOL.maxProfit(L[:])
        res2 = SOL.maxProfitArray(L[:])
        print(res,res2)
        count+=res==res2
    print(f"{count} out of {len(tests)} tests passed")


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()

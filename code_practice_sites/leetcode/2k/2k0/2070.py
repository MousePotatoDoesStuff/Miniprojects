import bisect
from typing import *
import inspect


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        prices = []
        maxB = {}
        while items:
            price, beauty = items.pop()
            if price in maxB:
                maxB[price] = max(maxB[price], beauty)
                continue
            prices.append(price)
            maxB[price] = beauty
        prices.sort(reverse=True)
        best_prices = [0]
        best_beauties = [0]
        while prices:
            cur_price = prices.pop()
            cur_beauty = maxB.pop(cur_price)
            if cur_beauty <= best_beauties[-1]:
                continue
            best_prices.append(cur_price)
            best_beauties.append(cur_beauty)
        RES = []
        for price in queries:
            next_ind = bisect.bisect_right(best_prices, price)
            best_beauty = best_beauties[next_ind - 1]
            RES.append(best_beauty)
        return RES

    main = maximumBeauty


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

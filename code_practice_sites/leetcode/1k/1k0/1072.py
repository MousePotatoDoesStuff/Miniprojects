from collections import defaultdict
from typing import *
import inspect


def listToInt(L):
    key=0
    while L:
        key<<=1
        key|=L.pop()
    return key

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter=defaultdict(int)
        mask=1<<len(matrix[0])
        mask-=1
        while matrix:
            L=matrix.pop()
            key=listToInt(L)
            if key&1:
                key^=mask
            counter[key]+=1
        return max(counter.values())

    main = maxEqualRowsAfterFlips


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

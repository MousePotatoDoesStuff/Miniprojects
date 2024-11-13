from typing import *
import inspect


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ongoing=[(0,-1)]
        best=0
        heights.append(0)
        for i,e in enumerate(heights):
            last=i
            while ongoing[-1][0]>e:
                height,start=ongoing.pop()
                cur=(i-start)*height
                if best<cur:
                    best=cur
                last=start
            if ongoing[-1][0]<e:
                ongoing.append((e,last))
        return best

    main = largestRectangleArea


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

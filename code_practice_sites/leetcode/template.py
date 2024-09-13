from typing import *
import inspect


class Solution:
    """
    Solulu.
    """
    def __init__(self):
        self.test = "test"

    def Template(self, L: List, i: int):
        return self.test

    main = Template


TESTS = [
    (([0, 1], 1), "test"),
    (([0, 1], 2), "test")
]


def do_tests(tests):
    """

    :param tests:
    """
    SOL = Solution()
    for i, (args, true_res) in enumerate(tests):
        print(f"Test {i + 1}")
        res = SOL.main(*args)
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return

if __name__ == "__main__":
    main()

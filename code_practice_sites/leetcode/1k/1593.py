from typing import *
import inspect


class Solution:
    def __init__(self):
        self.best: int = 0
        self.curlist: list = []

    def step(self, c):
        NEX = []
        while self.curlist:
            used, cur = self.curlist.pop()
            used: set
            cur += c
            NEX.append((used, cur))
            if cur in used:
                continue
            used=used|{cur}
            NEX.append((used, ''))
            self.best = max(self.best, len(used))
        self.curlist += NEX
        return

    def maxUniqueSplit(self, s: str) -> int:
        self.curlist = []
        self.best = 0
        start = set(), ''
        self.curlist.append(start)
        for c in s:
            self.step(c)
        return self.best

    main = maxUniqueSplit


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

from typing import *
import inspect


def removeExcess(s):
    last = ''
    res = ''
    for e in s:
        if e + last != '**':
            res += e
        last = e
    return res


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = removeExcess(p)
        if not s:
            return p in '*'
        if p[-1] == '*':
            s += '*'
        cur = [0]
        n = len(p)
        for e in s:
            nex = set()
            while cur:
                elind = cur.pop()
                if elind == n:
                    continue
                el = p[elind]
                if el == '*':
                    nex.add(elind)
                    cur.append(elind + 1)
                    el = '?'
                if el in e + '?':
                    nex.add(elind + 1)
            cur = list(nex)
        return n in cur

    main = isMatch


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

from typing import *
import inspect

VOWELS = {e: 1<<i for i, e in enumerate('aeiou@')}


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first = {0: 0}
        last = {0: 0}
        s += '@'
        status = 0
        for i, e in enumerate(s):
            if e not in VOWELS:
                continue
            wow_ind = VOWELS[e]
            last[status] = i
            status ^= wow_ind
            if status not in first:
                first[status] = i+1
        best = 0
        for e, v2 in last.items():
            v1 = first[e]
            best = max(v2 - v1, best)
        return best

    main = findTheLongestSubstring


TESTS = [
    (
        ("eleetminicoworoep",),
        13
    )
    ,
    (
        ("leetcodeisgreat",),
        5
    )
    ,
    (
        ("bcbcbc",),
        6
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

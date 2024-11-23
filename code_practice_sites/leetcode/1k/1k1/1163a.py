from typing import *
import inspect

class Solution:
    def lastSubstring(self, s: str) -> str:
        res_index = 0
        start = 1
        isleading=False
        for ind in range(1,len(s)):
            current: str = s[ind]
            ref: str = s[res_index + ind - start]
            if ref < current:
                res_index = start
                isleading=True
                continue
            if ref > current:
                start=ind+1
                isleading=True
                continue
            if current!=s[res_index]:
                isleading=False
                continue
            if isleading:
                continue
            start=ind
            isleading=True
        return s[res_index:]

    main = lastSubstring


TESTS = [
    (("abab",), "bab"),
    (("xxbbxxbx",), "xxbx"),
    (('cacacb',),'cb')
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    print("Running...")
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
    do_tests(TESTS, False)
    return


if __name__ == "__main__":
    main()

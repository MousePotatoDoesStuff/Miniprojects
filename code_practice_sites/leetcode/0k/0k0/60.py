from typing import *
import inspect


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        L = []
        for i in range(1, n + 1):
            k, p = divmod(k, i)
            L.append(p)
        X = [i + 1 for i in range(n)]
        res = ''
        while L:
            ind = L.pop()
            val = X.pop(ind)
            res += str(val)
        return res

    main = getPermutation


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
    sol = Solution()
    for i in range(1, 11):
        print(sol.getPermutation(4, i))
    return


if __name__ == "__main__":
    main()

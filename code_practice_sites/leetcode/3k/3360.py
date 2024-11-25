import math
from typing import *
import inspect


s=-0.5
r=-10.5
p=55.125-1
class Solution:
    def canAliceWin(self, n: int) -> bool:
        step=(n-p)/s
        step=math.sqrt(step)
        return int(r-step)%2

    main = canAliceWin


TESTS = [

]
def do_acc():
    acc = 0
    cur = False
    SOL=Solution()
    for i in range(10, 0, -1):
        for j in range(i):
            print(int(SOL.canAliceWin(acc)),end='')
            acc += 1
        print()
        cur=not cur


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
    do_acc()
    # do_tests(TESTS)
    return


if __name__ == "__main__":
    main()

from typing import *
import inspect


class Count:
    def __init__(self, s):
        cur = s[0]
        first = 0
        s += ' '
        self.values = []
        for i, e in enumerate(s):
            if e != cur:
                self.values.append((cur, i - first))
                cur = e
                first = i
        self.size = len(self.values)

    def getRemainingCount(self, A: tuple[int, int]):
        if A[0] not in range(self.size):
            return 0
        return self.values[A[0]][1] - A[1]

    def compare(self, A:tuple, B:tuple):
        a:str = self.values[A[0]][0]
        b:str = self.values[B[0]][0]
        return (a < b) - (a > b)

    def getMinRemaining(self, A, B):
        len1 = self.getRemainingCount(A)
        len2 = self.getRemainingCount(B)
        return min(len1, len2)

    def step(self, A, n):
        i, j = A
        j += n
        if j == self.values[i][1]:
            i += 1
            j = 0
        return i, j

    def minstep(self, A, B):
        steplen = self.getMinRemaining(A, B)
        A = self.step(A, steplen)
        B = self.step(B, steplen)
        return A, B

    def display_tail(self, ind):
        res=''
        for i in range(ind, self.size):
            cur = self.values[i]
            res += cur[0] * cur[1]
        return res


class Solution:
    def lastSubstring(self, s: str) -> str:
        last = 0
        C = Count(s)
        for i in range(1, C.size):
            d = 0
            temp = i, 0
            lastemp = last, 0
            while temp[0] != C.size:
                d = C.compare(lastemp, temp)
                if d != 0:
                    break
                lastemp, temp = C.minstep(lastemp, temp)
            if d == 1:
                last = i
        res = C.display_tail(last)
        return res

    main = lastSubstring


TESTS = [
    (("abab",),"bab"),
    (("xxbbxxbx",),"xxbx")
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
    do_tests(TESTS,False)
    return


if __name__ == "__main__":
    main()

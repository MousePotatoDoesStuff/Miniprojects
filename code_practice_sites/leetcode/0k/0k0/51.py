from typing import *
import inspect


def solveForStep(T, n):
    m = len(T)
    busy = set()

    for e in T:
        if e >= m:
            busy.add(e - m)
        if n - e > m:
            busy.add(e + m)
        busy.add(e)
        m -= 1
    RES = set()
    for i in range(n):
        if i not in busy:
            RES.add(T + (i,))
    return RES


def solveBulkForStep(S, n):
    new = set()
    for T in S:
        temp = solveForStep(T, n)
        new |= temp
    return new


def makeSolution(T, n):
    X = []
    for i in range(n):
        L = ['.'] * n
        L[T[i]] = 'Q'
        X.append(''.join(L))
    return X


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        start = tuple([])
        cur = {start}
        for i in range(n):
            cur = solveBulkForStep(cur,n)
        return [makeSolution(T, n) for T in cur]

    main = solveNQueens


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
    A=(3,)
    print(solveForStep(A,4))
    return


if __name__ == "__main__":
    main()

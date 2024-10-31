from typing import *


def accSum(M):
    ACM = []
    m = len(M[0]) + 1
    EXTRA = [0] * m
    LAST = EXTRA
    for L in M:
        ACL = []
        last = 0
        for i, e in enumerate(L):
            cur = int(e == 0)
            cur += last + LAST[i] - LAST[i - 1]
            ACL.append(cur)
            last = cur
        ACL.append(0)
        ACM.append(ACL)
        LAST = ACL
    ACM.append(EXTRA)
    return ACM


def checkSquare(ACM, ei, ej):
    n = min(ei, ej) + 1
    for k in range(1, n + 1):
        aa = ACM[ei - k][ej - k]
        ab = ACM[ei - k][ej]
        ba = ACM[ei][ej - k]
        bb = ACM[ei][ej]
        cur = aa + bb - ab - ba
        if cur != 0:
            return k-1
    return n


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ACM = accSum(matrix)
        for e in ACM:
            print(e)
        res = 0
        for i, L in enumerate(matrix):
            for j, e in enumerate(L):
                if e == 0:
                    continue
                cur = checkSquare(ACM, i, j)
                res += cur
        return res

    main = countSquares


TESTS = [
    (
        ([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]],),
        15)
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

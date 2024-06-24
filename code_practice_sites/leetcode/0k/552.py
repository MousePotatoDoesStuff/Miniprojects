from typing import *
import numpy


class Solution:
    attendanceMatrix = numpy.array([
        [1,1,0,1,0,0],
        [1,0,1,1,0,0],
        [1,0,0,1,0,0],
        [0,0,0,1,1,0],
        [0,0,0,1,0,1],
        [0,0,0,1,0,0]
    ], dtype=int)

    def checkRecord(self, n: int) -> int:
        MOD = int(1e9 + 7)
        attendance = numpy.array([1,0,0,0,0,0], dtype=int)
        mulmat = self.attendanceMatrix

        while n > 0:
            n, r = divmod(n, 2)
            if r:
                attendance = numpy.dot(attendance, mulmat) % MOD
            if n:
                mulmat = numpy.dot(mulmat, mulmat) % MOD

        return int(numpy.sum(attendance) % MOD)


    main = checkRecord


def test():
    return (2,), 3


def main():
    SOL = Solution()
    args, true_res = test()
    res = SOL.main(*args)
    print("Got {} ({})".format(res, type(res)))
    print("Expected {} ({})".format(true_res, type(true_res)))
    return


if __name__ == "__main__":
    main()

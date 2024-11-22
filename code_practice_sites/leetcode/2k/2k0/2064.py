from typing import *
import inspect


def numberOfStoresRequired(Q,maxPerStore):
    res=0
    for e,v in Q.items():
        res-=(-e//maxPerStore)*v
    return res
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if len(quantities)==1:
            return -(-quantities[0]//n)
        a=b=0
        Q={}
        for e in quantities:
            if b<e:
                b=e
            a+=e
            Q[e]=1+Q.get(e,0)
        a=-(-a//n)
        while a<b:
            c=a+b
            c//=2
            vc=numberOfStoresRequired(Q,c)
            print(a,b,c,vc)
            if vc>n:
                a=c+1
            else:
                b=c
        return a

    main = minimizedMaximum


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

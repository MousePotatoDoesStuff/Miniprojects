import bisect
from typing import *
import inspect


def groupOverlapIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=tuple,reverse=True)
    groups=[]
    curend=intervals[-1][0]
    while intervals:
        a,b=intervals.pop()
        if a>=curend:
            E=[]
            groups.append(E)
        E=groups[-1]
        E.append([a,b])
        curend=max(curend,b)
    return groups
def setMin(D,k,v):
    old=D.get(k,v+1)
    if v<old:
        D[k]=v
def unoverlapGroup(group):
    start=group[0][0]
    overlaps={start:0}
    for a,b in group:
        new={}
        for z,count in overlaps.items():
            if z<=a:
                setMin(new,b,count)
            setMin(new,z,count+1)
        overlaps=new
    return min(overlaps.values())
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        groups=groupOverlapIntervals(intervals)
        print(groups)
        res=0
        for e in groups:
            res+=unoverlapGroup(e)
        return res

    main = eraseOverlapIntervals


TESTS = [
    (
        ([[1,2],[2,3],[3,4],[1,3]],),
        1
    ),
    (
        ([[1,2],[1,2],[1,2],[1,4],[1,4],[1,4]],),
        5
    )

]


def do_tests(tests):
    """

    :param tests:
    """
    SOL = Solution()
    for i, (args, true_res) in enumerate(tests):
        print(f"Test {i + 1}")
        res = SOL.main(*args)
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))


def main():
    """

    :return:
    """
    do_tests(TESTS[1:])
    return

if __name__ == "__main__":
    main()

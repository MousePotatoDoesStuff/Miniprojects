from collections import defaultdict
from typing import *
import inspect


class Solution:
    def processQuery(self, start, end):
        self.specials[start].add(end)
        L = [(end, self.distances[start] + 1)]
        while L:
            cur, dis = L.pop()
            old = self.distances[cur]
            if dis >= old:
                continue
            self.distances[cur] = dis
            dis += 1
            if cur == self.n:
                continue
            temp = [cur + 1] + list(self.specials[cur])
            while temp:
                E = temp.pop(), dis
                L.append(E)
        return self.distances[-1]

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        self.n = n-1
        self.distances = list(range(n))
        self.specials = defaultdict(set)
        queries.reverse()
        RES = []
        while queries:
            Q = queries.pop()
            res = self.processQuery(*Q)
            RES.append(res)
        return RES

    main = shortestDistanceAfterQueries


TESTS = [
    (
        (5, [[2,4],[0,2],[0,4]]),
        "test")
    ,
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
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()

from typing import List
from heapq import heappush, heappop


class Solution(object):
    def __init__(self):
        self.heights: List[List[int]] = [[]]
        self.effort: List[List[int]] = [[]]

    def checkValidity(self, E):
        i, j = E
        if i not in range(len(self.heights)):
            return False
        L = self.heights[i]
        if j not in range(len(L)):
            return False
        return True

    def getHeight(self, E):
        i, j = E
        return self.heights[i][j]

    def setValue(self, E, v):
        i, j = E
        L = self.effort[i]
        if L[j] <= v:
            return False
        L[j] = v
        return True

    def setNeighbors(self, E, nxt):
        i, j = E
        h1 = self.getHeight(E)
        v1 = self.effort[i][j]
        X = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for F in X:
            if not self.checkValidity(F):
                continue
            h2 = self.getHeight(F)
            dev = abs(h1 - h2)
            v2 = max(dev, v1)
            if self.setValue(F, v2):
                nxt.append((v2, F))
        return

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        MAX = 10 ** 9
        self.heights = heights
        self.effort = [[MAX for f in e] for e in heights]
        self.effort[0][0] = 0
        cur = []
        heappush(cur, (0, (0, 0)))
        goal = (len(heights) - 1, len(heights[0]) - 1)
        i = 0
        while True:
            _, E = heappop(cur)
            if E == goal:
                return self.effort[E[0]][E[1]]
            L = []
            self.setNeighbors(E, L)
            for EL in L:
                heappush(cur, EL)


def test1():
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    return Solution().minimumEffortPath(heights)


def test2():
    heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    return Solution().minimumEffortPath(heights)


def main():
    print(test2())
    return


if __name__ == "__main__":
    main()

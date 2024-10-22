from typing import *


def buildLR(conds):
    L = {}
    R = {}
    for a, b in conds:
        L[b] = set()
        R[a] = set()
    while conds:
        a, b = conds.pop()
        L[b].add(a)
        R[a].add(b)
    return L, R


def getOrder(k, conds):
    left, right = buildLR(conds)
    stack = [e for e in right if e not in left]
    res = []
    remaining = set(range(1,k+1))
    while stack:
        cur = stack.pop()
        nexts = right.pop(cur) if cur in right else set()
        res.append(cur)
        remaining.remove(cur)
        for e in nexts:
            left[e] -= {cur}
            if not left[e]:
                left.pop(e)
                stack.append(e)
    if left:
        return None
    res.extend(list(remaining))
    return res


def invertOrder(order):
    X = [0] * (len(order) + 1)
    for i, e in enumerate(order):
        X[e] = i
    return X


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowOrder = getOrder(k, rowConditions)
        colOrder = getOrder(k, colConditions)
        if not (rowOrder and colOrder):
            return []
        rowloc = invertOrder(rowOrder)
        colloc = invertOrder(colOrder)
        mat = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            a, b = rowloc[i], colloc[i]
            mat[a][b] = i
        return mat

    main = buildMatrix


def test():
    return (3, [[1,2],[3,2]], [[2,1],[3,2]]), "test"


def main():
    SOL = Solution()
    args, true_res = test()
    res = SOL.main(*args)
    print("Got {} ({})".format(res, type(res)))
    print("Expected {} ({})".format(true_res, type(true_res)))
    return


if __name__ == "__main__":
    main()

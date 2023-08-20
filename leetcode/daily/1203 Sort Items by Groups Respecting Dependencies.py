from typing import List


def set_dict_set(D, k, v):
    S = D.get(k, set())
    S.add(v)
    D[k] = S
    return


def validate_dependencies(items: set, dependencies: dict):
    n=len(items)
    dependent = {e: set() for e in items}
    for e in dependencies:
        if len(dependencies[e]) == 0:
            continue
        items.remove(e)
    items = list(items)
    for e, S in dependencies.items():
        for f in S:
            dependent[f].add(e)
    RES = []
    while len(items) > 0:
        cur = items.pop()
        RES.append(cur)
        S = dependent.pop(cur)
        for e in S:
            T = dependencies[e]
            T: set
            T.remove(cur)
            if len(T) == 0:
                dependencies.pop(e)
                items.append(e)
    if len(RES)!=n:
        return None
    return RES


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groupDependencies = dict()
        itemDependencies = {i: dict() for i in range(m)}
        for i in range(n):
            if group[i] == -1:
                group[i] = -1 - i
                itemDependencies[-1 - i] = dict()
        for i in range(n):
            gi = group[i]
            curDep = itemDependencies[gi]
            CS = set()
            curDep[i] = CS
            for e in beforeItems[i]:
                f = group[e]
                if f == gi:
                    CS.add(e)
                else:
                    set_dict_set(groupDependencies, gi, f)
        curGroups = [e for e in itemDependencies if e not in groupDependencies]
        Seq = validate_dependencies(set(itemDependencies.keys()), groupDependencies)
        if Seq is None:
            return []
        RES = []
        for e in Seq:
            GD = itemDependencies[e]
            if e<0:
                RES.append(-1 - e)
                continue
            GD: dict
            L = validate_dependencies(set(GD.keys()), GD)
            if L is None:
                return []
            RES.extend(L)
        return RES


def case1():
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[1], [6], [5], [6], [3, 6], [], [], []]
    res = Solution().sortItems(n, m, group, beforeItems)


def main():
    A = {0, 1, 2}
    B = {0: {0, 1}, 1: {0}}
    res = validate_dependencies(A, B)
    print(res)
    print()
    case1()
    return


if __name__ == "__main__":
    main()

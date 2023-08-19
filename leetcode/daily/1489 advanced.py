from typing import List


class Solution:
    def __init__(self):
        self.edges = None

    def findCombinations(self, used, edges):
        D=dict()
        for E in edges:
            for i in [0,1]:
                if E[i] in used:
                    continue
                D[E[i]]=D.get(E[i],set())
                D[E[i]].add((E[1-i],E[2]))
        M=[({e:e for e in D},[])]
        for E in edges:
            a=E[0]
            b=E[1]
            for EL,X in M:
                EL=EL.copy()
                if a not in EL:
                    a,b=b,a
                if b not in EL:
                    EL[a]=None
                else:
                    b=EL[b]
                    if b==EL[a]:
                        continue
                    if EL[a] not in (a,None):
                        EL[EL[a]]=b
                    EL[a]=b
                M.append((EL,X+[E[2]]))
        return

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        X = set()
        D = dict()
        self.edges = edges
        for i, e in enumerate(edges):
            v = e[2]
            S = D.get(v, set())
            S.add(i)
            D[v] = S
            X.add(v)
        X = list(X)
        X.sort()
        print(X, D)
        used = set()
        crit = set()
        pseudo = set()
        return [[], []]


def main():
    X = [0]
    return


if __name__ == "__main__":
    main()

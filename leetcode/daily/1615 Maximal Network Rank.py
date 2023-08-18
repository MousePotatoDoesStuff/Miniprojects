from typing import List


class Solution:
    def check_sym(self, links, A):
        for (i, e) in enumerate(A):
            for f in A[i + 1:]:
                if f not in links[e]:
                    return True
        return False

    def check(self, links, A, B):
        for e in A:
            for f in B:
                if f not in links[e]:
                    return True
        return False

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) == 0:
            return 0
        links = {i: set() for i in range(n)}
        for (a, b) in roads:
            links[a].add(b)
            links[b].add(a)
        m = 0
        L = [(-4, -4)]
        for (k, v) in links.items():
            E = (len(v), k)
            m = max(m, E[0])
            L.append(E)
        L.sort()
        E, A, B, C = L.pop(), [], [], []
        while E[0] == m:
            A.append(E[1])
            E = L.pop()
        while E[0] == m - 1:
            B.append(E[1])
            E = L.pop()
        while E[0] == m - 2:
            C.append(E[1])
            E = L.pop()
        A.sort()
        B.sort()
        C.sort()
        if len(A) > 1:
            if self.check_sym(links, A):
                return m * 2
            else:
                return m * 2 - 1
        if len(B) > 0:
            if self.check(links, A, B):
                return m * 2 - 1
            else:
                return m * 2 - 2
        if len(C) > 0:
            if self.check(links, A, C):
                return m * 2 - 2
            else:
                return m * 2 - 3
        ma = A[0]
        va, vb = E
        while E[0] == va:
            E = L.pop()
            if E[1] not in links[ma]:
                return m + va
        return m + va - 1


def main():
    return


if __name__ == "__main__":
    main()

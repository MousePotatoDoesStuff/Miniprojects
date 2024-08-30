from heapq import heappush, heappop
from typing import List

INF = float("inf")


def toGraph(n, edges):
    G = [dict() for i in range(n)]
    for a, b, w in edges:
        if w == -1:
            continue
        G[a][b] = w
        G[b][a] = w
    return G


class Solution:
    def dijkstra(self):
        E = (self.start, 0)
        H = [E]
        res = [INF for e in self.G]
        while H:
            cur, val = heappop(H)
            if res[cur] <= val:
                continue
            res[cur] = val
            if cur == self.end:
                break
            for nex, jump in self.G[cur].items():
                E = (nex, jump + val)
                heappush(H, E)
        return res[self.end]

    def modifiedGraphEdges(self, n: int, edges: List[List[int]],
                           source: int, destination: int, target: int) -> List[List[int]]:
        self.G = G = toGraph(n, edges)
        self.start = source
        self.end = destination
        distance = self.dijkstra()
        res = []
        if distance < target:
            print("Unsolvable")
            return res
        for e in edges:
            if e[2] != -1:
                continue
            a, b, _ = e
            e[2] = 1
            G[a][b] = 1
            G[b][a] = 1
            if distance == target:
                continue
            distance = self.dijkstra()
            if distance <= target:
                e[2] += target - distance
                distance = target
        return edges


def main():
    return


if __name__ == "__main__":
    main()

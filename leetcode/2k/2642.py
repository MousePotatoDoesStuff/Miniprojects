import heapq
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]], INF=10**9+7):
        self.INF=INF
        self.M=[[INF for _j in range(n)] for _i in range(n)]
        while edges:
            E=edges.pop()
            self.M[E[0]][E[1]]=E[2]
        return

    def addEdge(self, edge: List[int]) -> None:
        self.M[edge[0]][edge[1]]=edge[2]
        return

    def shortestPath(self, node1: int, node2: int) -> int:
        X=[(0,node1)]
        while X:
            E=heapq.heappop(X)
            if E[1]==node2:
                return E[0]
            L=self.M[E[1]]
            for j,f in enumerate(L):
                if f is self.INF:
                    continue
                heapq.heappush(X,(E[0]+f,j))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)


def main():
    return


if __name__ == "__main__":
    main()

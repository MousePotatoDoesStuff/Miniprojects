class Solution(object):
    def groupShorten(self, groups, start):
        X = [start]
        cur = start
        while groups[cur] != cur:
            cur = groups[cur]
            X.append(cur)
        while len(X) > 0:
            groups[X.pop()] = cur
        return

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        connections = []
        n = len(points)
        print(n)
        for i in range(n):
            for j in range(i + 1, n):
                A = points[i]
                B = points[j]
                h = abs(A[0] - B[0]) + abs(A[1] - B[1])
                connections.append((h, i, j))
        connections.sort(reverse=True)
        groups = [i for i in range(n)]
        connSum = 0
        while len(connections) > 0:
            h, i, j = connections.pop()
            self.groupShorten(groups, i)
            self.groupShorten(groups, j)
            if groups[i] == groups[j]:
                continue
            groups[groups[j]] = groups[i]
            groups[j] = groups[i]
            connSum += h
        return connSum


def main():
    S = Solution()
    GR = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    res=S.minCostConnectPoints(GR)
    print(res)
    return


if __name__ == "__main__":
    main()

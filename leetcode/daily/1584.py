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
        print(connections)
        groups = [i for i in range(n)]
        connSum = 0
        while len(connections) > 0:
            h, i, j = connections.pop()
            print(h, i, j, groups, end="|")
            self.groupShorten(groups, i)
            self.groupShorten(groups, j)
            print(groups, end="|")
            if groups[i] == groups[j]:
                print("NO", i, j)
                continue
            m = len([i for i in range(n) if groups[i] == i])
            groups[groups[j]] = groups[i]
            groups[j] = groups[i]
            connSum += h
            m2 = len([i for i in range(n) if groups[i] == i])
            if m != m2:
                print(h, i, j, (m, m2), groups)
            else:
                print(h, i, j)
        return connSum


def main():
    S = Solution()
    GR = [0, 0, 1, 2, 3, 4]
    for i in range(5, -1, -1):
        S.groupShorten(GR, i)
        print(GR)
    return


if __name__ == "__main__":
    main()

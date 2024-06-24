from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        INF = 1 << 31
        L = []
        while quality:
            a = quality.pop()
            b = wage.pop()
            L.append((b / a, a))
        L.sort(reverse=True)
        MH = []
        qs = 0
        max_r = 0.0
        for i in range(k):
            r, q = L.pop()
            qs += q
            if max_r < r:
                max_r = r
            heapq.heappush(MH, -q)
        res = max_r * qs
        while L:
            r, q = L.pop()
            if max_r < r:
                max_r = r
            qs += q + heapq.heappop(MH)
            heapq.heappush(MH, -q)
            mrqs = max_r * qs
            if res > mrqs:
                res = mrqs
        return res


def main():
    return


if __name__ == "__main__":
    main()

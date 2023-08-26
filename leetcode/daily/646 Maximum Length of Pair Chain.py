from collections import deque
from typing import List


class Solution:

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        self.pairs = pairs
        starts = dict()
        ends = dict()
        nums = {-1001}
        for a, b in pairs:
            if starts.get(a, b) >= b:
                starts[a] = b
            if ends.get(b, a) <= a:
                ends[b] = a
            nums |= {a, b}
        nums = sorted(nums)
        cur_nums = deque()
        cur_best = dict()
        for e in nums:
            if e in starts:
                f = starts[e]
                v = 0
                for i in range(len(cur_nums)):
                    e2 = cur_nums[i]
                    if e2 >= e:
                        break
                    v = max(cur_best[e2] + 1, v)
                for i in range(len(cur_nums)):
                    if cur_nums[-1]<f:
                        break
                    cur_best.pop(cur_nums.pop())
                cur_best[f] = v
                cur_nums.append(f)
            if e in ends:
                f = ends[e]
                while cur_nums[0] < f:
                    cur_best.pop(cur_nums.popleft())
        return max(cur_best.values())


def main():
    ex = [[1,2],[2,3],[3,4]]
    res = Solution().findLongestChain(ex)
    print(res)
    return


if __name__ == "__main__":
    main()

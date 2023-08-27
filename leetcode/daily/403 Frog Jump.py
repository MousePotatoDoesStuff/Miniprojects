from collections import deque
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jump_from = {0: {0}}
        for current in stones:
            passed = set()
            new = set()
            for last_stone in jump_from:
                d = current - last_stone
                D = {d - 1, d, d + 1}
                R = jump_from[last_stone] & D
                if len(R) == 0:
                    if max(jump_from[last_stone]) < d - 1:
                        passed.add(last_stone)
                    continue
                new.add(d)
            if len(new) != 0:
                jump_from[current] = new
            for e in passed:
                jump_from.pop(e)
        return len(jump_from.get(stones[-1],{}))!=0


def main():
    X = [0, 1, 2, 3, 4, 8, 9]
    res = Solution().canCross(X)
    print(res)
    return


if __name__ == "__main__":
    main()

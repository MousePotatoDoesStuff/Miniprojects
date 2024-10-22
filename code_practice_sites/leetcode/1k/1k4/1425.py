from typing import List


class SlidingMax:
    def __init__(self, L, k):
        self.M = [L]
        self.k = k
        cur = L
        while len(cur) > 1:
            L2 = []
            c2 = None
            k2 = 0
            for e in cur:
                if c2 is None:
                    c2 = e
                if e > c2:
                    c2 = e
                k2 += 1
                if k2 == k:
                    L2.append(c2)
                    c2 = None
                    k2 = 0
            if c2 is not None:
                L2.append(c2)
            cur = L2
            self.M.append(L2)

    def change(self, index, value):
        if index not in range(len(self.M[0])):
            return False
        for level, L in enumerate(self.M):
            if len(L) == 1:
                L[0] = value
                return
            new, rem = divmod(index, self.k)
            a = index - rem
            L[index] = value
            value = self.check(level, a, a + self.k, value)
            index //= self.k

    def check(self, level, start, end, res):
        L = self.M[level]
        if end>len(L):
            end=len(L)
        for i in range(start, end):
            if res < L[i]:
                res = L[i]
        return res

    def getmax(self, start, end, default=None):
        if end > len(self.M[0]):
            end = len(self.M[0])
        if start < 0:
            start = 0
        res = self.M[0][start]
        if default is not None:
            res=default
        for level in range(len(self.M)):
            firstlim = start - (start % self.k) + self.k
            secondlim = end - (end % self.k)
            if firstlim >= secondlim:
                if start < end:
                    res = self.check(level, start, end, res)
                return res
            res = self.check(level, start, firstlim, res)
            res = self.check(level, secondlim, end, res)
            start = firstlim // self.k
            end = secondlim // self.k


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        m=max(nums)
        if m<=0:
            return m
        X = SlidingMax(nums, 10)
        for i in range(len(nums)):
            X.change(i, X.getmax(i - k, i, 0)+nums[i])
            print(X.M)
        return X.M[-1][-1]


def main():
    S = Solution()
    L = [-7609,249,-1699,2385,9125,-9037,1107,-8228,856,-9526]
    X = SlidingMax(L, 5)
    for e in X.M:
        print(e)
    k = 9
    res = S.constrainedSubsetSum(L, k)
    print(res)
    return


if __name__ == "__main__":
    main()

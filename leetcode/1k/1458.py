from typing import List


class Solution:
    def maxDotProductPositive(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        prevs = [(-1, 0)]
        for i, e in enumerate(nums1):
            nexts = []
            prevs += [(m + 1, float("inf"))]
            pr_ind = 0
            for j, f in enumerate(nums2):
                while prevs[pr_ind][0] < j:
                    nexts.append(prevs[pr_ind])
                    pr_ind += 1
                E = (j, prevs[pr_ind-1][1] + e * f)
                if prevs[pr_ind][0] == j:
                    E = max(E, prevs[pr_ind])
                    pr_ind += 1
                nexts.append(E)
            prevs = []
            last = -1
            for e in nexts:
                if e[1]>last:
                    prevs.append(e)
                    last=e[1]
            prevs.pop()
        return prevs[-1][1]

    def filter(self, nums):
        plus = []
        minus = []
        zero = False
        for e in nums:
            if e > 0:
                plus.append(e)
                continue
            if e < 0:
                minus.append(-e)
                continue
            zero = True
        return plus, minus, zero

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        plus1, minus1, zero1 = self.filter(nums1)
        plus2, minus2, zero2 = self.filter(nums2)
        if not ((plus1 and plus2) or (minus1 and minus2)):
            best = -(10**9+7)
            if zero1 or zero2:
                return 0
            if plus1 and minus2:
                best = max(best, -min(plus1) * min(minus2))
            if plus2 and minus1:
                best = max(best, -min(plus2) * min(minus1))
            return best
        best=0
        if plus1 and plus2:
            best=max(best,self.maxDotProductPositive(plus1,plus2))
        if minus1 and minus2:
            best=max(best,self.maxDotProductPositive(minus1,minus2))
        return best


def main():
    SOL=Solution()
    res=SOL.maxDotProduct([2,1,-2,5],[3,0,-6])
    print(res)
    return


if __name__ == "__main__":
    main()

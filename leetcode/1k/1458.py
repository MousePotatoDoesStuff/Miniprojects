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
                add = e * f
                if add <= 0:
                    continue
                E = (j, prevs[pr_ind - 1][1] + add)
                if prevs[pr_ind][0] == j:
                    E = max(E, prevs[pr_ind])
                    pr_ind += 1
                nexts.append(E)
            prevs.pop()
            for j in range(pr_ind,len(prevs)):
                nexts.append(prevs[j])
            prevs = []
            last = -1
            for e in nexts:
                if e[1] > last:
                    prevs.append(e)
                    last = e[1]
        return prevs[-1][1]

    def filter(self, nums):
        other = []
        zero = False
        for e in nums:
            if e == 0:
                zero = True
                continue
            other.append(e)
        return other, zero

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, zero1 = self.filter(nums1)
        nums2, zero2 = self.filter(nums2)
        a1, b1 = min(nums1),max(nums1)
        a2, b2 = min(nums2), max(nums2)
        if b1 < 0 < a2:
            if zero1 or zero2:
                return 0
            return b1*a2
        if b2 < 0 < a1:
            if zero1 or zero2:
                return 0
            return b1*a2
        return self.maxDotProductPositive(nums1,nums2)


def main():
    SOL = Solution()
    res = SOL.maxDotProduct([3,-2], [2,-6,7])
    print(res)
    return


if __name__ == "__main__":
    main()

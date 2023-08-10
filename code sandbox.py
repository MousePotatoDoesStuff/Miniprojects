from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        D = dict()
        for i,e in enumerate(nums):
            L=D.get(e,[])
            L.append(i)
            D[e]=L
        R = set()
        zero = 0
        for zero in range(n):
            if nums[zero] >= 0:
                break
        zero_right = zero
        for zero_right in range(zero,n):
            if nums[zero_right] > 0:
                break
        else:
            zero_right=n
        print(zero,zero_right)
        if zero_right - zero >= 3:
            R.add((0, 0, 0))
        for i in range(zero):
            e=nums[i]
            for j in range(zero_right, n):
                f=nums[j]
                s=-e-f
                if s in D:
                    for k in D[s]:
                        if i<k<j:
                            R.add((e,s,f))
                            print(e,s,f)
                            break
                print(i, j, '|', s)
        return [list(E) for E in R]


def main():
    X = Solution()
    print(X.threeSum([0,0,0]))


if __name__ == "__main__":
    main()

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        M=dict()
        for i in range(len(nums)):
            e=nums[i]
            if e not in M:
                M[e]=i
            if target-e in M:
                j=M[target-e]
                if j!=i:
                    return [j,i]


def main():
    X=Solution()
    print(X.twoSum([3,3],6))
    return


if __name__ == "__main__":
    main()

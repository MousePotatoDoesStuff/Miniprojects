from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestMinimum=prices[0]
        bestProfit=0
        for e in prices:
            bestMinimum=min(bestMinimum,e)
            f=e-bestMinimum
            bestProfit=max(bestProfit,f)
        return bestProfit


def main():
    X = Solution()
    return


if __name__ == "__main__":
    main()

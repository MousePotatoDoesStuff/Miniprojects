import bisect
import itertools
import math
from typing import List


def count(D:list, target, n):
    ans = 0
    for i in range(1, n + 1):
        for lcm in D[i]:
            ans += target // lcm * pow(-1, i + 1)
    return ans


def generateList(L: list[tuple], new_el):
    return [E + (new_el,) for E in L]


def generateCombs(coins: list[int]):
    X = [[1]]
    for i in range(1, len(coins)+1):
        E=[]
        for comb in itertools.combinations(coins, i):
            E.append(math.lcm(*comb))
        X.append(E)
    return X

def filterCoins(coins):
    coins.sort()
    newcoins = []
    for e in coins:
        for f in newcoins:
            if e % f == 0:
                break
        else:
            newcoins.append(e)
    return newcoins


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = filterCoins(coins)
        combs = generateCombs(coins)
        n=len(coins)
        start, end = min(coins), min(coins) * k
        while start + 1 < end:
            mid = (start + end) // 2
            if count(combs, mid, n) >= k:
                end = mid
            else:
                start = mid
        if count(combs, start, n) >= k:
            return start
        else:
            return end


def main():
    sol=Solution()
    print(filterCoins([6,1,2,4]))
    for i in range(1,1):
        res=sol.findKthSmallest([5,2],i)
        print(res)
    return


if __name__ == "__main__":
    main()

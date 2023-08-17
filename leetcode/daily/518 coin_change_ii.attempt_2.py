from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.nxt = dict()
        self.log = dict()
        self.coins=[]

    def add_value(self, amount, coins, count):
        if amount < 0:
            return
        n = len(self.nxt)
        X: set = self.nxt.get(amount,set())
        self.nxt[amount]=X
        e = (amount, coins)
        self.log[e] = self.log.get(e, 0) + count
        X.add(coins)
        return
    def process_value(self,amount,coins):
        count=self.log.pop((amount,coins))
        for i in range(coins+1):
            self.add_value(amount-self.coins[i],i,count)
        return
    def process(self):
        key=max(self.nxt.keys())
        if key==0:
            return False
        X=self.nxt[key]
        for e in X:
            self.process_value(key,e)
        self.nxt.pop(key)
        return True

    def change(self, amount: int, coins: List[int]) -> int:
        self.nxt.clear()
        self.nxt[0]=set()
        self.log.clear()
        self.coins=coins
        self.add_value(amount, len(coins) - 1, 1)
        while self.process():
            pass
        return sum(self.log.values())


def main():
    sol=Solution()
    res =sol.change(4003, [4001,4002,4003,4004,4005])
    print(res)
    res =sol.change(5000, [4001,4002,4003,4004,4005])
    print(res)
    return


if __name__ == "__main__":
    main()

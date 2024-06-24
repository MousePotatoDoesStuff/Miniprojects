import bisect
from typing import *


class DescendingBest:
    def __init__(self):
        self.L=[]
    def append(self,E):
        L=self.L
        if not L:
            L.append(E)
            return True
        lo,hi=E
        if lo<L[-1][0]:
            return False
        while L and L[-1][1]<=hi:
            L.pop()
        L.append(E)
        return True
    def combine(self,other):
        other:DescendingBest
        X=self.L
        self.L=[]
        Y=other.L
        while Y:
            X.append(Y.pop())
        X.sort(reverse=True)
        while X:
            self.append(X.pop())
        return
    def apply(self,E):
        newL=[]
        L=self.L
        limit=bisect.bisect_left(L,(E[0],-1))
        for i in range(limit):
            lo,hi=L[i]
            new=lo,hi+E[1]
            newL.append(new)
        if limit!=len(L):
            _,hi=L[-1]
            new=E[0],hi+E[1]
            newL.append(new)
        res=DescendingBest()
        res.L=newL
        return res
    def getMaxProd(self):
        k=0
        for lo,hi in self.L:
            p=lo*hi
            if k<p:
                k=p
        return k



class Solution:
    def step(self,E):
        last=DescendingBest()
        for cur in self.subs:
            step=cur.apply(E)
            cur.combine(last)
            last=step
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        INF=1000000
        self.subs=[DescendingBest() for i in range(k+1)]
        self.subs[0].append((INF,0))
        for i,hi in enumerate(nums1):
            lo=nums2[i]
            E=(lo,hi)
            self.step(E)
        return self.subs[-1].getMaxProd()
    main=maxScore

def test():
    return ([1,3,3,2],[2,1,3,4],3),12



def main():
    SOL=Solution()
    args,true_res=test()
    res=SOL.main(*args)
    print("Got {} ({})".format(res,type(res)))
    print("Expected {} ({})".format(true_res,type(true_res)))
    return


if __name__ == "__main__":
    main()
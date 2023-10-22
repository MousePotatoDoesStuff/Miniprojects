import heapq
from typing import List


class Solution:
    def Left(self):
        worst=self.nums[self.k]
        Q=[]
        for i in range(self.k-1,-1,-1):
            e=self.nums[i]
            if e<worst:
                Q.append((self.k-i-1,worst))
                worst=e
        Q.append((self.k,worst))
        return Q
    def Right(self):
        worst=self.nums[self.k]
        Q=[]
        n=len(self.nums)
        for i in range(self.k+1,n):
            e=self.nums[i]
            if e<worst:
                Q.append((i-self.k-1,worst))
                worst=e
        Q.append((n-self.k-1,worst))
        return Q
    def generate(self,left,right,a2,b2):
        if a2 == len(left) or b2==len(right):
            return (0,a2,b2)
        L=left[a2]
        R=right[b2]
        E=(-(L[0]+R[0]+1)*min(L[1],R[1]),a2,b2)
        return E
    def maximumScore(self, nums: List[int], k: int) -> int:
        self.nums=nums
        self.k=k
        left=self.Left()
        right=self.Right()
        worst=min(left[-1][1],right[-1][1])
        lim_r=len(nums)-k-1
        X=[(-nums[k],0,0)]
        best=nums[k]
        while True:
            anti,a,b=heapq.heappop(X)
            if anti==0:
                break
            if best<-anti:
                best=-anti
            heapq.heappush(X,self.generate(left,right,a+1,b))
            heapq.heappush(X,self.generate(left,right,a,b+1))
        return best


def main():
    S=Solution()
    res=S.maximumScore([1,4,3,7,4,5],3)
    print(res)
    return


if __name__ == "__main__":
    main()

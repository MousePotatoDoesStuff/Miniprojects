from collections import deque
from typing import List

def tuplify(E):
    if type(E)==int:
        return E,1
    return E
def untuplify(E):
    if E[1]==1:
        return E[0]
    return E

class IntervalList:
    def __init__(self,raw:List):
        self.Q=deque()
        raw.append(-2)
        last=-1
        lastInd=0
        for i,e in enumerate(raw):
            if e!=last:
                count=i-lastInd
                if count==1:
                    self.Q.append(last)
                else:
                    self.Q.append((last,count))
                last=e
                lastInd=i
        self.Q.popleft()
    def popFirst(self):
        A=self.Q.popleft()
        if type(A)==int:
            return A
        A,n=A
        if n==2:
            self.Q.appendleft(A)
        else:
            self.Q.appendleft((A,n-1))
        return A
    def popLast(self):
        A=self.Q.pop()
        if type(A)==int:
            return A
        A,n=A
        if n==2:
            self.Q.append(A)
        else:
            self.Q.append((A,n-1))
        return A
    def step(self,other,k):
        other:IntervalList
        if not other.Q:
            return 0
        self.popLast()
        newQ=deque()
        curel,cursize=0,0
        counter=0
        for other_el in other.Q:
            other_el,other_size=tuplify(other_el)
            while other_size>0:
                if cursize==0:
                    curel,cursize=tuplify(self.Q.popleft())
                newsize=min(other_size,cursize)
                cursize-=newsize
                other_size-=newsize
                tempres=curel*other_el
                if tempres not in range(1,k):
                    tempres=0
                else:
                    counter+=newsize
                if newQ and tuplify(newQ[-1])[0]==tempres:
                    newsize+=tuplify(newQ.pop())[1]
                newQ.append(untuplify((tempres,newsize)))
        self.Q=newQ
        other.popFirst()
        return counter





class Solution:
    def naive(self,nums,k):
        curproducts = [1 for i in range(len(nums) + 1)]
        res = 0
        lastres = 0
        for i in range(len(nums)):
            curproducts.pop()
            for j, e in enumerate(curproducts):
                e *= nums[i + j]
                if e not in range(1,k):
                    e = 0
                else:
                    res += 1
                curproducts[j] = e
            if res == lastres:
                break
            lastres = res
        return res
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res=0
        numsProcessed=IntervalList(nums)
        if len(numsProcessed.Q)>=len(nums)*1.5:
            return self.naive(nums,k)
        acc=IntervalList([])
        acc.Q.append((1,len(nums)+1))
        tempres=-1
        while tempres!=0:
            tempres=acc.step(numsProcessed,k)
            res+=tempres
        return res


def run(inputargs: tuple):
    SOL = Solution()
    res = SOL.numSubarrayProductLessThanK(*inputargs)
    print(res)


def main():
    # run(([10,5,2,6],100))
    run(([10,2,2,5,4,4,4,3,7,7],289))
    return


if __name__ == "__main__":
    main()

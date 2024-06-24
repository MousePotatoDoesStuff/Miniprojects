import bisect
from typing import List


class Solution:
    def __init__(self):
        self.arr = None
        self.k = None
        self.R = None
        self.rayT = None

    def determineSmallerCount(self, coef:float):
        curind=0
        arr=self.arr
        n=len(arr)
        res=0
        tops=[]
        for i,e in enumerate(arr):
            while curind<n:
                f=arr[curind]
                if f>e*coef:
                    tops.append(curind)
                    res+=curind-int(f>=e)
                    break
                curind+=1
            else:
                res+=(n-1)*(n-i)
        return tops,res
    def IntervalStep(self,a):
        n=len(self.arr)
        ratio=self.rayT[a]
        tops,res=self.determineSmallerCount(ratio)
        if res<=self.k:
            for i in range(len(tops)):
                L=self.R[i]
                L[0]=tops[i]
            for i in range(len(tops),len(self.R)):
                self.R[i]=n
        else:
            for i in range(len(tops)):
                L=self.R[i]
                L[1]=tops[i]
        return res

    def returnEdge(self,val):
        c=self.arr[-1]
        if val>1:
            return [c,int(c/val+0.5)]
        return [int(val*c+0.5),c]


    def findIntervals(self):
        a=0
        b=len(self.rayT)
        curmin=0
        while b-a>1:
            c=(a+b)//2
            res=self.IntervalStep(c)
            d=res-self.k
            if d==0:
                return self.returnEdge(self.rayT[c])
            if d>0:
                b=c
            else:
                a=c
                curmin=res
        X=[]
        print(self.R)
        for i,den in enumerate(self.arr):
            a,b=self.R[i]
            for nin in range(a,b):
                num=self.arr[nin]
                if num==den:
                    continue
                X.append((num/den,num,den))
        X.sort()
        E=X[self.k-curmin]
        print("X",X,"\n",self.k,curmin,E)
        return [E[1],E[2]]

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        self.arr=arr
        self.k=k
        biggest=arr[-1]
        n=len(arr)
        self.rayT=[e/biggest for e in arr]
        self.rayT.pop()
        self.rayT.extend([biggest/e for e in arr][::-1][1:])
        print(self.rayT)
        print(self.determineSmallerCount(2/5))
        self.R=[[0,n] for _ in arr]
        res=self.findIntervals()
        return res


def main():
    SOL=Solution()
    res=SOL.kthSmallestPrimeFraction([1,2,3,5],3)
    print(res)
    return


if __name__ == "__main__":
    main()

class MountainArray:
    def __init__(self,L):
        self.L=L
    def get(self,index):
        return self.L[index]
    def length(self):
        return len(self.L)
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation (what if I need to test it on my computer tho lol)
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def enumCall(self,k):
        if k not in range(self.n):
            return (k,-1)
        E=(k,self.marr.get(k))
        print(E)
        return E
    def BinSearch(self,A,B,target,reverse):
        if B[1]==target:
            return B[0]
        if A[1]==target:
            return A[0]
        C=A
        while B[0]-A[0]>1:
            C=self.enumCall((A[0]+B[0])//2)
            d=C[1]-target
            if d==0:
                return C[0]
            if (d>0)^reverse:
                A=(C[0]+1,-3)
            else:
                B=(C[0],-3)
        return C[0] if C[1]==target else -1
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        self.marr=mountain_arr
        self.n=self.marr.length()
        A=self.enumCall(0)
        B=self.enumCall(self.n-1)
        if A[1]==target:
            return 0
        C=None
        D=None
        lastA=A
        lastB=B
        limA=None
        limB=None
        while B[0]-A[0]>1:
            if A[1]<target:
                lastA=A
            if B[1]<target:
                lastB=B
            print(A,C,D,B)
            v=max(1,int((B[0]-A[0])*0.382))
            C=self.enumCall(A[0]+v)
            D=self.enumCall(B[0]-v)
            print(":",A,C,D,B)
            diff=C[1]-D[1]
            aTargeted=bTargeted=1
            if diff==0:
                A=C
                B=D
                C=None
                D=None
                print("->->",A,C,D,B)
            if diff<0:
                A=C
                C=D
                D=None
                bTargeted=0
            if diff>0:
                B=D
                D=C
                C=None
                aTargeted=0
            if aTargeted and A[1]>=target:
                if A[1]==target:
                    return A[0]
                if limA is None:
                    limA=A
            if bTargeted and B[1]>=target:
                if limB is None:
                    limB=B
            if None not in (limA,limB):
                break
        if None in (limA,limB):
            print("NONE:",lastA,limA,limB,lastB)
            return A[0] if A[1]==target else -1
        res1=self.BinSearch(lastA,limA,target,False)
        if res1>=0:
            return res1
        res2=self.BinSearch(limB,lastB,target,True)
        return res2

def main():
    MONT=MountainArray([3,5,3,2,0])
    SOL=Solution()
    res=SOL.findInMountainArray(0,MONT)
    print(res)
    return


if __name__ == "__main__":
    main()

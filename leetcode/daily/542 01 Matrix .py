from typing import List


class Solution:
    def __init__(self):
        self.m = None
        self.n = None
        self.mat = None

    def isValidPlace(self,i,j):
        return (i in range(self.n)) and (j in range(self.m))
    def getNonZero(self):
        res=set()
        for i in range(self.n):
            for j in range(self.m):
                if self.mat[i][j]!=0:
                    res.add((i,j))
        return res
    def isFlat(self,i,j):
        ref=self.mat[i][j]
        for (di,dj) in [(0,1),(0,-1),(1,0),(-1,0)]:
            ki,kj=i+di,j+dj
            if not self.isValidPlace(ki,kj):
                continue
            if self.mat[ki][kj]<ref:
                return False
        return True
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.mat=mat
        n=len(mat)
        m=len(mat[0])
        self.n=n
        self.m=m
        active=self.getNonZero()
        while len(active)>0:
            not_active=set()
            for (i,j) in active:
                if not self.isFlat(i,j):
                    not_active.add((i,j))
            active-=not_active
            for (i,j) in active:
                self.mat[i][j]+=1
        return self.mat





def main():
    return


if __name__ == "__main__":
    main()

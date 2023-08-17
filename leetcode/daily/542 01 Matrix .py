class Solution:
    def isValidPlace(self,i,j):
        return (i in range(self.n)) and (j in range(self.n))
    def getNonZero(self):
        res=set()
        for i in range(self.n):
            for j in range(self.m):
                if self.mat[i][j]!=0:
                    res.add((i,j))
        return res
    def isFlat(self):
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
        self.res=[[ for j in range(m)]for i in range(n)]
        self.active=getNonZero()
        while len(self.active)>0:
            


def main():
    return


if __name__ == "__main__":
    main()

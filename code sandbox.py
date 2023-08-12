from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        X=[0 for i in range(m+1)]
        X[0]=1
        print(n,m)
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]:
                    X[j]=0
                X[j+1]+=X[j]
            print(X)
        return X[-2]


def main():
    X = Solution()
    res=X.uniquePathsWithObstacles([[1,0,0],[0,0,0],[0,0,0]])
    print(res)


if __name__ == "__main__":
    main()

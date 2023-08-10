from typing import List


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        cur=x
        res=1
        while n>0:
            if n&1:
                res*=cur
            cur*=cur
            n//=2
        return res



def main():
    X = Solution()
    print(X.myPow(2,9))


if __name__ == "__main__":
    main()

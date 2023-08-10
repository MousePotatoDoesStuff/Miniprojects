from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        n=len(nums)
        if nums[0]>nums[-1]:
            a=0
            b=n
            while b-a>1:
                c=(a+b)//2
                if nums[c]>nums[a]:
                    a=c
                else:
                    b=c
            start=b
        shift=lambda x:(x+start)%n
        a=0
        b=n
        while b-a>1:
            c=(b+a)//2
            d=nums[shift(c)]-target
            if d==0:
                return shift(c)
            elif d>0:
                b=c
            else:
                a=c
        res=shift(a)
        return res if nums[res]==target else -1


def main():
    X = Solution()
    L=[4,5,6,7,0,1,2]
    for e in L+[3]:
        res=X.search(L,e)
        print(res)
    return


if __name__ == "__main__":
    main()

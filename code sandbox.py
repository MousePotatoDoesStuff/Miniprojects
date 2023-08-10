from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        for k in range(m+n-1,-1,-1):
            if j<0:
                break
            if i<0 or nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
                continue
            nums1[k]=nums1[i]
            i-=1
            continue
        return



def main():
    X = Solution()
    A=[1,3,5,7,0,0,0]
    B=[2,4,6]
    X.merge(A,4,B,3)
    print(A)


if __name__ == "__main__":
    main()

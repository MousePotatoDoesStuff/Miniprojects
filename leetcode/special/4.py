from bisect import bisect


def EndList(n,L):
    return n if n>=0 else len(L)


class Solution(object):
    def __init__(self):
        self.extras = []

    def findMedian(self,L,delta=0,start=0,end=-1,get_indices=False):
        end=EndList(end,L)
        n=end-start+abs(delta)
        half=(n-1)//2
        half+=start
        if delta<0:
            half+=delta
        other=half if n&1 else half+1
        if get_indices:
            self.extras.append((self,other))
        return L[half] if half==other else (L[half]+L[other])/2
    def findFirst(self, nums1, nums2, start1=0, start2=0, end1=-1, end2=-1):
        end1=EndList(end1,nums1)
        end2=EndList(end2,nums2)
        A1=nums1[start1]
        A2=nums2[start2]
        swc=False
        if A1>A2:
            swc=True
            nums1,nums2=nums2,nums1
            start1,start2=start2,start1
            end1,end2=end2,end1
            A1,A2=A2,A1
        B1=nums1[end1-1]
        B2=nums2[end2-1]
    def findGroupStartOverlap(self, nums1, nums2, start1=0, start2=0, end1=-1, end2=-1):
        end1=EndList(end1,nums1)
        end2=EndList(end2,nums2)
        A1=nums1[start1]
        A2=nums2[start2]
        swc=False
        if A1>A2:
            swc=True
            nums1,nums2=nums2,nums1
            start1,start2=start2,start1
            end1,end2=end2,end1
            A1,A2=A2,A1
        B1=nums1[end1-1]
        B2=nums2[end2-1]
        if B1<=A2:
            return None,swc
        res1 = start1
        res2 = start2
        if A1<=A2:
            res1=bisect(nums1,A2)
        if A2>=A1:
            res2=bisect(nums2,A1)
        return (res2,res1) if swc else (res1,res2)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


def main():
    sol=Solution()
    A=[1,2,3,4,5]
    B=[3,4,5,6,7]
    res=sol.findGroupStartOverlap(A,B)
    print(res)
    return


if __name__ == "__main__":
    main()

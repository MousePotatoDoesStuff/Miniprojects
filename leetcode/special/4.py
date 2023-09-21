class Solution(object):
    def __init__(self):
        self.extras = []

    def findMedian(self,L,delta=0,get_indices=False):
        n=len(L)+abs(delta)
        half=(n-1)//2
        if delta<0:
            half+=delta
        other=half if n&1 else half+1
        if get_indices:
            self.extras.append((self,other))
        return L[half] if half==other else (L[half]+L[other])/2
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


def main():
    sol=Solution()
    d=-2
    print(sol.findMedian([1,4,5,7,22],d))
    print(sol.findMedian([1,4,5,7,22,69,420,1337],d))
    return


if __name__ == "__main__":
    main()

import bisect


def EndList(n, L):
    return n if n >= 0 else len(L)


def SwapIf(s, swc):
    return (s[1], s[0]) if swc else s


class Solution(object):
    def __init__(self):
        self.extras = []

    def findMedian(self, L, delta=0, start=0, end=-1, get_indices=False, alt=0):
        end = EndList(end, L)
        n = end - start + abs(delta)
        half = (n - 1) // 2
        half += start
        if delta < 0:
            half += delta
        other = half if n & 1 else half + 1
        if get_indices:
            self.extras.append((half, other))
        vother= 1.0*(L[other] if other in range(start,end) else alt)
        return L[half] if half == other else (L[half] + vother) / 2.0

    def findGroupStartOverlap(self, nums1, nums2, start1, start2):
        A1 = nums1[start1]
        A2 = nums2[start2]
        res1 = start1
        res2 = start2
        if A1 <= A2:
            res1 = bisect.bisect_left(nums1, A2)
        if A2 <= A1:
            res2 = bisect.bisect_left(nums2, A1)
        return res1, res2

    def findGroupEndOverlap(self, nums1, nums2, end1, end2):
        B1 = nums1[end1 - 1]
        B2 = nums2[end2 - 1]
        res1 = end1
        res2 = end2
        if B1 >= B2:
            res1 = bisect.bisect_right(nums1, B2)
        if B2 >= B1:
            res2 = bisect.bisect_right(nums2, B1)
        return res1, res2

    def findGroupOverlap(self, nums1, nums2, start1, start2, end1, end2):
        swc = False
        if nums1[start1] > nums2[start2]:
            swc = True
            nums1, nums2 = nums2, nums1
            start1, start2 = start2, start1
            end1, end2 = end2, end1
        if nums1[end1 - 1] < nums2[start2]:
            return None, swc
        start_overlap = self.findGroupStartOverlap(nums1, nums2, start1, start2)
        end_overlap = self.findGroupEndOverlap(nums1, nums2, end1, end2)
        return SwapIf(start_overlap, swc), SwapIf(end_overlap, swc)

    def medianSplit(self, nums1, nums2, start1, start2, end1, end2, delta=0):
        mid_1 = self.findMedian(nums1, delta, start1, end1, True)
        med_a1, med_b1 = self.extras.pop()
        mid_2 = self.findMedian(nums2, delta, start2, end2, True)
        med_a2, med_b2 = self.extras.pop()
        diff = mid_2 - mid_1
        if diff >= 0:
            start1 = med_a1
        if diff <= 0:
            start2 = med_a2
        diff = nums2[med_b2] - nums1[med_b1]
        if diff <= 0:
            end1 = med_b1 + 1
        if diff >= 0:
            end2 = med_b2 + 1
        return (start1, end1), (start2, end2)

    def medianFinisher(self, nums1, nums2, start1, start2, end1, end2, delta=0):
        n = end1+end2-start1-start2
        last = 420.69
        if delta < 0:
            delta *= -1
            n += delta
            while delta <= n - delta:
                if start1 == end1:
                    return self.findMedian(nums2, -delta, start2, end2, alt=last)
                if start2 == end2:
                    return self.findMedian(nums1, -delta, start1, end1, alt=last)
                a = nums1[start1]
                b = nums2[start2]
                if a > b:
                    cur = b
                    start2 += 1
                else:
                    cur = a
                    start1 += 1
                if delta == n - delta:
                    last += cur
                    last /= 2.0
                else:
                    last = cur
                delta += 1
        else:
            n += delta
            while delta <= n - delta:
                if start1 == end1:
                    return self.findMedian(nums2, delta, start2, end2, alt=last)
                if start2 == end2:
                    return self.findMedian(nums1, delta, start1, end1, alt=last)
                a = nums1[end1 - 1]
                b = nums2[end2 - 1]
                if a < b:
                    cur = b
                    end2 -= 1
                else:
                    cur = a
                    end1 -= 1
                if delta == n - delta:
                    last += cur
                    last /= 2.0
                else:
                    last = cur
                delta += 1
        return last

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        start1 = 0
        start2 = 0
        end1 = len(nums1)
        end2 = len(nums2)
        if 0 in (end1, end2):
            if end1 == 0:
                nums1 = nums2
            return self.findMedian(nums1)
        s_ov, e_ov = self.findGroupOverlap(nums1, nums2, start1, start2, end1, end2)
        if s_ov is None:
            if e_ov:
                nums1, nums2 = nums2, nums1
                start1, start2 = start2, start1
                end1, end2 = end2, end1
            d = len(nums2) - len(nums1)
            if d == 0:
                return (nums1[-1] + nums2[0])/2.0
            if d > 0:
                delta = -len(nums1)
                nums1 = nums2
            else:
                delta = len(nums2)
            return self.findMedian(nums1, delta)
        delta = 0
        new1=s_ov[0],e_ov[0]
        new2=s_ov[1],e_ov[1]
        last=69.420
        if new2[1]!=end2:
            last=nums2[new2[1]]
        if new1[1]!=end1:
            last=nums1[new1[1]]
        while True:
            delta -= sum(new1) + sum(new2)
            delta += start1 + start2 + end1 + end2
            start1, end1 = new1
            start2, end2 = new2
            len1 = end1 - start1
            len2 = end2 - start2
            if 0 in (len1, len2):
                if len1 == 0:
                    return self.findMedian(nums2,delta,start2,end2,alt=last)
                return self.findMedian(nums1,delta,start1,end1,alt=last)
            if max(len1, len2) < 4:
                return self.medianFinisher(nums1, nums2, start1, start2, end1, end2, delta)
            else:
                new1, new2 = self.medianSplit(nums1, nums2, start1, start2, end1, end2, delta)


def main():
    sol = Solution()
    nums1 =[1,3]
    nums2 =[2]
    res = sol.findMedianSortedArrays(nums1,nums2)
    # res = sol.(A, B, 0, 0, len(A), len(B), 0)
    print(res)
    return


if __name__ == "__main__":
    main()

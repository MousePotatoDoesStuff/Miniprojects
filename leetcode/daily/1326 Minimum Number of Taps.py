from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        ranges=[(max(i-e,0),min(i+e,n)) for (i,e) in enumerate(ranges) if e!=0]
        ranges.sort(key=lambda e:(e[0],-e[1]))
        if len(ranges)==0:
            return -1

        L=[ranges[0]]
        last=-1
        for i in range(1,len(ranges)):
            if ranges[i][0]!=last:
                last=ranges[i][0]
                L.append(ranges[i])
        ranges=L
        last_coverage=-1
        coverage=0
        count=0
        for i in range(len(ranges)):
            if ranges[i][0]>coverage:
                return -1
            if coverage<ranges[i][1]:
                if last_coverage<ranges[i][0]:
                    count+=1
                    last_coverage=coverage
                coverage=ranges[i][1]
        if coverage<n:
            return -1
        return count


def main():
    ranges=[4,0,0,0,0,0,0,0,4]
    res=Solution().minTaps(len(ranges)-1,ranges)
    print(res)
    return


if __name__ == "__main__":
    main()

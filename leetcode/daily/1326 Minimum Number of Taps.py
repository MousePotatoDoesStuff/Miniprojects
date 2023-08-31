from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        for (i,e) in enumerate(ranges):
            ranges[i]=(i-e,i+e)
        ranges.sort(key=lambda e:(e[0],-e[1]))

        j=0
        for i in range(1,n+1):
            if ranges[i][0]!=ranges[j][0] and ranges[i][0]!=ranges[i][1]:
                j+=1
                ranges[j]=ranges[i]
        for i in range(j,n):
            ranges.pop()
        last_coverage=-1
        coverage=0
        j=0
        for i in range(len(ranges)):
            if ranges[i][0]>coverage:
                return -1
            if coverage<ranges[i][1]:
                if last_coverage<ranges[i][0]:
                    j+=1
                    last_coverage=coverage
                ranges[j]=ranges[i]
                coverage=ranges[i][1]
        for i in range(j,len(ranges)):
            ranges.pop()
        return 0


def main():
    ranges=[0,1,2,1,0]
    res=Solution().minTaps(4,ranges)
    return


if __name__ == "__main__":
    main()

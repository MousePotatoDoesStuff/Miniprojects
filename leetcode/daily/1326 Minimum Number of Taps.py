from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        ranges=[(max(i-e,0),i+e) for (i,e) in enumerate(ranges) if e!=0]
        ranges.sort(key=lambda e:(e[0],-e[1]))

        j=0
        print(ranges)
        for i in range(1,len(ranges)):
            if ranges[i][0]!=ranges[j][0] and ranges[i][0]!=ranges[i][1]:
                j+=1
                ranges[j]=ranges[i]
        print(ranges,j,n)
        while len(ranges)>j+1:
            ranges.pop()
        print(ranges,j,n)
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
        if coverage<n:
            return -1
        for i in range(j,len(ranges)):
            ranges.pop()
        return len(ranges)


def main():
    ranges=[3,4,1,1,0,0]
    res=Solution().minTaps(5,ranges)
    print(res)
    return


if __name__ == "__main__":
    main()

from typing import *


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        curXorCounts = {}
        curXor = 0
        res = 0
        for i, e in enumerate(arr):
            lastXor = curXor
            curXor ^= e
            if curXor in curXorCounts:
                lastind, acc, count=curXorCounts[curXor] # last index, pre-increment amount, occurence count
                res+=acc+(i-lastind)*count
            lastind, acc, count=curXorCounts.get(lastXor,(0,0,0))
            acc+=(i-lastind)*count
            count+=1
            curXorCounts[lastXor]=(i,acc,count)
            print(i,lastXor,curXor,curXorCounts)
        return res

    main=countTriplets

def test():
    return ([2,3,1,6,7],),4



def main():
    SOL=Solution()
    args,true_res=test()
    res=SOL.main(*args)
    print("Got {} ({})".format(res,type(res)))
    print("Expected {} ({})".format(true_res,type(true_res)))
    return


if __name__ == "__main__":
    main()

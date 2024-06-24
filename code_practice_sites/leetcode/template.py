from typing import *


class Solution:
    def __init__(self):
        self.test="test"
    def Template(self, L:List,i:int):
        return self.test
    main=Template

def test():
    return ([0,1],1),"test"



def main():
    SOL=Solution()
    args,true_res=test()
    res=SOL.main(*args)
    print("Got {} ({})".format(res,type(res)))
    print("Expected {} ({})".format(true_res,type(true_res)))
    return


if __name__ == "__main__":
    main()

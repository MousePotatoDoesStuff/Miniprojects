import heapq
from typing import *
from typing import Tuple, Dict, Any, Set

from PIL.ImageChops import offset


class TreeNode:
    """
    treeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.best = None
        self.nodes = None
        self.n = None
        self.heights = []
        self.depths = []
        self.root = None
        return

    def countNodes(self):
        cur=[self.root]
        n=0
        while cur:
            e=cur.pop()
            if not e:
                continue
            n+=1
            cur+=[e.left,e.right]
        return n

    def heiAndDep(self,node:TreeNode,dep=0):
        if not node:
            return -1
        val=node.val-1
        self.nodes[val]=node
        self.depths[val]=dep
        dep+=1
        hei=-1
        for e in (node.left,node.right):
            cuhei=self.heiAndDep(e,dep)
            hei=max(hei,cuhei)
        hei+=1
        self.heights[val]=hei
        return hei

    def bestDepths(self):
        n=max(self.depths)+1
        X=[[-1]*2 for _ in range(n)]
        for i in range(self.n):
            dep=self.depths[i]
            hei=self.heights[i]
            L=X[dep]
            for j in range(2):
                if L[j]<hei:
                    L[j],hei=hei,L[j]
        self.best=X
        return

    def doQuery(self,nodeind):
        depth=self.depths[nodeind]
        best_hei=self.best[depth]
        if best_hei[1]==-1:
            return depth-1
        height=self.heights[nodeind]
        if best_hei[0]==height:
            depth+=max(0,best_hei[1])
        else:
            depth+=best_hei[0]
        return depth


    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.root = root
        self.n=n=self.countNodes()
        self.heights=[0]*n
        self.depths=[0]*n
        self.nodes=[root]*n
        self.heiAndDep(self.root)
        self.bestDepths()
        RES = []
        for que in queries:
            new_height=self.doQuery(que-1)
            RES.append(new_height)
        return RES

    main = treeQueries


TESTS = [
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    for i, (args, true_res) in enumerate(tests):
        res = SOL.main(*args)
        count += res == true_res
        if only_show_errors and res == true_res:
            continue
        print(f"Test {i + 1}")
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))
    print(f"{count} out of {len(tests)} tests passed")


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()

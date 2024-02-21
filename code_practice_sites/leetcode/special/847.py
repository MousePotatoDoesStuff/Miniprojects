from typing import List, Tuple


class NodeStatus:
    def __init__(self,index,neighbours):
        self.index=index
        self.paths:List[Tuple[set,list]]=[]
        return
    def apply_path(self):


# https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        X=[set() for i in range(len(graph))]
        tryAll=True
        for i,e in enumerate(graph):
            if len(e)==1:
                X[i].update((i,))
                tryAll=False
        if tryAll:
            X=[{(i,)}for i in range(len(graph))]


def main():
    return


if __name__ == "__main__":
    main()

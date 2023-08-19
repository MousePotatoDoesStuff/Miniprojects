from typing import List


class Vertex:
    def __init__(self,parent,path,level=0,group_parent=None):
        self.parent = parent
        self.path = path
        if parent is not None and level==0:
            level=parent.level+1
        self.level=level
        self.group_parent = group_parent
    def find_common_ancestor(self,other):
        p1:Vertex=self
        p2:Vertex=other
        while p1.parent is not p2.parent:
            while p1.level<p2.level:
                p2=p2.parent
            p1=p1.parent
        return p1,p2
    def group_all_until(self,target):
        target:Vertex
        cur:Vertex=self
        while cur is not target:
            cur.parent=target.parent
        return
class VertTree:
    def __init__(self):
        self.root=Vertex(None,None)
        self.used=dict()
        self.unused=dict()
    def add_link(self):
        return

class Solution:
    def __init__(self):
        self.edges = None

    def findEdgeCombinations(self,used,chosen):
        verts=dict()
        for e in chosen:
            E=self.edges[e]
            verts[E[0]]=(E[1],e)
            verts[E[1]]=(E[0],e)
        X=[]
        stack=[]




    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        X=set()
        D=dict()
        self.edges=edges
        for i,e in enumerate(edges):
            v=e[2]
            S=D.get(v,set())
            S.add(i)
            D[v]=S
            X.add(v)
        X=list(X)
        X.sort()
        print(X,D)
        used=set()
        crit=set()
        pseudo=set()
        return [[],[]]


def main():
    a=None
    b=None
    print(a==b,a is b)
    return


if __name__ == "__main__":
    main()

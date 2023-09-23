from typing import List


class StrTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.subvalues = dict()

    def compare(self, reference):
        reference: StrTreeNode
        mode = min(len(self.subvalues), 2)
        if mode == 0:
            return []
        res = dict()
        for e in reference.subvalues:
            res[e] = [False, True, None][mode * int(e in self.subvalues)]
        return list(res.items())

    def getTrue(self,reference):
        reference: StrTreeNode
        a=len(self.subvalues)
        b=len(reference.subvalues)
        if a*b==0:
            return []
        res = set()
        sva=self.subvalues
        svb=reference.subvalues
        if b<a:
            sva,svb=svb,sva
        for e in sva:
            if e in svb:
                res.add(e)
        return [(e,True) for e in res]



    def __repr__(self):
        s = str(self.value)
        if len(self.subvalues) != 0:
            s += '|' + str(self.subvalues)
        return "[{}]".format(s)


class StrTree:
    def __init__(self, v=None):
        self.root = StrTreeNode(v)

    def __repr__(self):
        return str(self.root)

    def append(self, s, v):
        current: StrTreeNode = self.root
        for c in s:
            new = current.subvalues.get(c, StrTreeNode())
            current.subvalues[c] = new
            current = new
        current.value = v
        return

    def check(self,s):
        current: StrTreeNode = self.root
        for c in s:
            current = current.subvalues.get(c, None)
            if current is None:
                return None
        return current.value

    def getValid(self, reference):
        res = []
        stack = [(self.root, reference.root, '', self.root.compare(reference.root))]
        while len(stack) > 0:
            thisNode, refNode, status, nexts = stack.pop()
            if (thisNode.value is not None) and (refNode.value is not None):
                res.append((thisNode.value, refNode.value))
            if len(nexts) == 0:
                continue
            nxt=nexts.pop()
            if nxt[1] is None:
                nexts.append((nxt[0],True))
            newL=(
                thisNode,
                refNode.subvalues[nxt[0]],
                nxt[0],
                thisNode.getTrue(refNode)
            ) if not nxt[1] else (
                thisNode.subvalues[nxt[0]],
                refNode.subvalues[nxt[0]],
                status,
                thisNode.compare(refNode)
            )
            stack.append(newL)


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        D = dict()
        lens = set()
        for i, e in enumerate(words):
            n = len(e)
            STR: StrTree = D.get(n, StrTree())
            STR.append(e, i)
            D[n] = STR
            lens.add(n)
        lens = list(lens)
        lens.sort(reverse=True)
        currents = {0: StrTree(0)}
        while len(lens) > 0:
            curlen = lens.pop()
            curRef = D[]
        return 0


def main():
    SOL = Solution()
    S = 'B AC BC ABC ADE'
    L = S.split()
    res = SOL.longestStrChain(L)
    return


if __name__ == "__main__":
    main()

from collections import deque
from typing import List


class StrTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.subvalues = dict()

    def check_against(self, reference):
        reference: StrTreeNode
        mode = min(len(reference.subvalues), 2)
        if mode == 0:
            return [(e, False) for e in self.subvalues]
        res = dict()
        X = [False, True, None]
        for e in self.subvalues:
            res[e] = X[mode * int(e in reference.subvalues)]
        return list(res.items())

    def getTrue(self, reference):
        reference: StrTreeNode
        a = len(self.subvalues)
        b = len(reference.subvalues)
        if a * b == 0:
            return []
        res = set()
        sva = self.subvalues
        svb = reference.subvalues
        if b < a:
            sva, svb = svb, sva
        for e in sva:
            if e in svb:
                res.add(e)
        return [(e, True) for e in res]

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

    def check(self, s):
        current: StrTreeNode = self.root
        for c in s:
            current = current.subvalues.get(c, None)
            if current is None:
                return None
        return current.value

    def getValid(self, reference, targetLen):
        res = []
        Q = deque()
        E = (self.root, reference.root, '', self.root.check_against(reference.root))
        Q.append(E)
        while len(Q) > 0:
            LQ = len(Q)
            thisNode, refNode, status, nexts = Q.popleft()
            thisNode: StrTreeNode
            refNode: StrTreeNode
            if (status!="") and (thisNode.value is not None) and (refNode.value is not None):
                v=refNode.value[0]+1
                if v==targetLen:
                    res.append((thisNode.value, refNode.value[0] + 1))
                    continue
            if len(nexts) == 0:
                continue
            for nxt in nexts:
                if nxt[1] is not True:
                    AT=thisNode.subvalues[nxt[0]]
                    BT=refNode
                    CT=AT.getTrue(BT)
                    newL = (AT,BT,nxt[0],CT)
                    Q.append(newL)
                if nxt[1] is not False:
                    AT=thisNode.subvalues[nxt[0]]
                    BT=refNode.subvalues[nxt[0]]
                    CT=AT.check_against(BT)
                    newL = (AT,BT,status,CT)
                    Q.append(newL)
        return res


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lens = set()
        STR = StrTree()
        for i, e in enumerate(words):
            STR.append(e, i)
            lens.add(len(e))
        lens = list(lens)
        lens.sort(reverse=True)
        currents = StrTree((0, None))
        while len(lens) > 0:
            curlen = lens.pop()
            valid = STR.getValid(currents,curlen)
            currents = StrTree(None)
            for (i, v) in valid:
                e = words[i]
                currents.append(e, (v, i))
        return 0


def tree_unit_tests(filt=None):
    if filt is None:
        filt = [1]
    T = [
        ((0, None),dict(), 'A B CD', 1),
        (None,{'A':1,'B':1},'A B CD EA', 2),
        (None,{'A':1,'B':1},'A B CD', 2)
    ]
    for i, (a, x, s, tl) in enumerate(T):
        if i not in filt:
            continue
        ref = StrTree(a)
        for e,v in x.items():
            ref.append(e,(v,e))
        main = StrTree()
        for e in s.split():
            main.append(e, e)
        res = main.getValid(ref, tl)
        print(res)


def main_test():
    SOL = Solution()
    S = 'B AC BC ABC ADE'
    L = S.split()
    res = SOL.longestStrChain(L)
    return


def main():
    # tree_unit_tests()
    main_test()
    return


if __name__ == "__main__":
    main()

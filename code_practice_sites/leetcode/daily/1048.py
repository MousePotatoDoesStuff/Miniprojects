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

    def check_plus1(self, s):
        found = []
        best = -1
        current: StrTreeNode = self.root
        for i, c in enumerate(s):
            branch = len(current.subvalues) - int(c in current.subvalues)
            if branch:
                found.extend([(current, i) for e in current.subvalues if e != c])
            nxt = current.subvalues.get(c, None)
            if nxt is None:
                found.append((current, i))
                break
            current = nxt
        else:
            for el in current.subvalues.values():
                if el.value is not None:
                    best = max(best, el.value)
        while len(found) > 0:
            current, j = found.pop()
            for c in s[j + 1:]:
                current = current.subvalues.get(c, None)
                if current is None:
                    break
            else:
                best = max(best, current.value[1]+1)
        return None if best<0 else best


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lens = set()
        D = dict()
        for i, e in enumerate(words):
            n = len(e)
            S = D.get(n, set())
            S.add(i)
            D[n] = S
            lens.add(n)
        lens = list(lens)
        lens.sort(reverse=True)
        currents = StrTree((0,0))
        best=0
        while len(lens) > 0:
            curlen = lens.pop()
            new_ones = StrTree()
            for i in D[curlen]:
                res = currents.check_plus1(words[i])
                if res is None:
                    res=1
                new_ones.append(words[i], (i,res))
                print(words[i], (i,res))
                best=max(best,res)
            currents = new_ones
        return best


def main():
    SOL = Solution()
    S = 'A A AAA AAAA AAAAA'
    L = S.split()
    res = SOL.longestStrChain(L)
    print(res)
    return


if __name__ == "__main__":
    main()

from typing import *


class WordTreeNode:
    def __init__(self, end: bool = False):
        self.end = end
        self.keys = {}

    def setdefault(self, c: str):
        if c not in self.keys:
            self.keys[c] = WordTreeNode()
        return self.keys[c]

    def step(self, c):
        return self.keys.get(c, None)


class WordTree:
    def __init__(self):
        self.root = WordTreeNode()

    def add(self, s):
        cur = self.root
        for e in s:
            cur = cur.setdefault(e)
        cur.end = True

    def step(self, node, lines: str, c):
        X = []
        if node is self.root and lines:
            lines += " "
        lines+=c
        nexnode = node.step(c)
        if nexnode is None:
            return []
        nexnode: WordTreeNode
        if nexnode.end:
            X.append((self.root, lines))
        X.append((nexnode, lines))
        return X


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        tree = WordTree()
        while wordDict:
            tree.add(wordDict.pop())
        curnodes = [(tree.root, "")]
        for e in s:
            newnodes = []
            while curnodes:
                node, lines = curnodes.pop()
                newnodes += tree.step(node, lines, e)
            curnodes = newnodes
            print([e[1] for e in curnodes])
        return [e[1] for e in curnodes if e[0] is tree.root]

    main = wordBreak


def test():
    A="catsanddog"
    B=["cat","cats","and","sand","dog"]
    C=["cats and dog","cat sand dog"]
    return (A,B), C


def main():
    SOL = Solution()
    args, true_res = test()
    res = SOL.main(*args)
    print("Got {} ({})".format(res, type(res)))
    print("Expected {} ({})".format(true_res, type(true_res)))
    return


if __name__ == "__main__":
    main()

from typing import *
import inspect


class TrieNode:
    def __init__(self):
        self.isFinal = -1
        self.next = {}

    def add(self, c):
        nex = self.next.get(c, TrieNode())
        self.next[c] = nex
        return nex

    def check(self, c):
        return self.next.get(c, None)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        cur = self.root
        for e in s:
            cur = cur.add(e)
        cur.isFinal = len(s)

    def step(self, L:List[TrieNode], c):
        NL = []
        for el in L:
            nel = el.check(c)
            if nel is None:
                continue
            NL.append(nel)
        NL.append(self.root)
        return NL


def main():
    return


if __name__ == "__main__":
    main()
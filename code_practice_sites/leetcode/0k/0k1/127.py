from typing import *


class TrieNode:
    def __init__(self):
        self.next = {}

    def add(self, c):
        nex = self.next.get(c, TrieNode())
        self.next[c] = nex
        return nex

    def check(self, c, default=None):
        res = self.next.get(c, default)
        return res


class Trie:
    def __init__(self, L: list[str]):
        self.root = TrieNode()
        while L:
            s = L.pop()
            self.add(s)

    def add(self, s):
        cur = self.root
        for e in s:
            cur = cur.add(e)

    def step(self, L: List[TrieNode], c):
        NL = []
        for el in L:
            nel = el.check(c)
            if nel is None:
                continue
            NL.append(nel)
        NL.append(self.root)
        return NL

    def check(self, s, cur=None):
        if cur is None:
            cur = self.root
        for e in s:
            cur = cur.check(e)
            if not cur:
                return False
        return True

    def findOneDiff(self, s, RES: set):
        cur: TrieNode = self.root
        X = list(s)
        X.reverse()
        prefix = ''
        for e in s:
            X.pop()
            remaining = ''.join(X)[::-1]
            for c, node in cur.next.items():
                if c == e:
                    continue
                if self.check(remaining, node):
                    RES.add(prefix + c + remaining)
            cur = cur.check(e, None)
            if not cur:
                break
            prefix += e
        return RES


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        T = Trie(wordList)
        used = set()
        cur = {beginWord}
        score = 1
        while cur:
            nex = set()
            for e in cur:
                T.findOneDiff(e, nex)
            score += 1
            if endWord in nex:
                return score
            nex -= used
            used |= cur
            cur = nex
        return 0

    main = ladderLength


TESTS = [
    (
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        5)
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    print("Running...")
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

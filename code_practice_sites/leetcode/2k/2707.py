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
        finals = set()
        for el in L:
            nel = el.check(c)
            if nel is None:
                continue
            if nel.isFinal > 0:
                finals.add(nel)
            NL.append(nel)
        NL.append(self.root)
        return NL, finals


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        T = Trie()
        while dictionary:
            s2 = dictionary.pop()
            T.add(s2)
        s2 = ""
        chk = [0] * 51
        cur = [T.root]
        for i, e in enumerate(s):
            cur, finals = T.step(cur,e)
            res = i + 1
            for di in finals:
                res = min(res, chk[i + 1 - di])
            chk[i + 1] = res
        return chk[len(s)]

    main = minExtraChar


TESTS = [
    (
        ([0, 1], 1),
        "test")
    ,
    (
        ([0, 1], 2),
        "also test"
    )
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

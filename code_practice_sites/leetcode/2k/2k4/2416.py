from typing import *
import inspect


class TrieNode:
    def __init__(self):
        self.count = 0
        self.next = {}

    def add(self, c):
        self.count += 1
        nex = self.next.get(c, TrieNode())
        self.next[c] = nex
        return nex

    def check(self, c, default=None):
        return self.next.get(c, default)


DEFAULTNODE = TrieNode()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        cur = self.root
        for e in s:
            cur = cur.add(e)
        cur.count += 1

    def check(self, s):
        cur = self.root
        res = 0
        for e in s:
            cur = cur.check(e, DEFAULTNODE)
            res += cur.count
        return res


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        T = Trie()
        for e in words:
            T.add(e)
        RES = []
        for e in words:
            res = T.check(e)
            RES.append(res)
        return RES

    main = sumPrefixScores


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

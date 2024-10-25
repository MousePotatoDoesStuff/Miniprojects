from typing import *
import inspect


class TrieNode:
    def __init__(self):
        self.final = False
        self.subnodes = dict()

    def setdefault(self, foldername: str):
        subnode: TrieNode = self.subnodes.get(foldername, TrieNode())
        self.subnodes[foldername] = subnode
        return subnode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, path: list[str]):
        cur: TrieNode = self.root
        for e in path:
            if cur.final:
                return False
            cur = cur.setdefault(e)
        cur.final=True
        return True


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda e:str.count(e,'/'))
        tracker = Trie()
        RES = []
        for foe in folder:
            sepath = foe.split("/")
            if tracker.add(sepath):
                RES.append(foe)
        return RES

    main = removeSubfolders


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

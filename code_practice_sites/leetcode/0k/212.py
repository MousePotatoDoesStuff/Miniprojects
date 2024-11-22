from typing import *
import inspect


class Node:
    def __init__(self):
        self.val = False
        self.subnodes = dict()

    def check(self, c):
        return self.subnodes.get(c, None)

    def add(self, c):
        if c not in self.subnodes:
            self.subnodes[c] = Node()
        return self.subnodes[c]


class WordDict:
    def __init__(self):
        self.root: Node = Node()

    def add(self, word: str):
        cur = self.root
        for c in word:
            cur = cur.add(c)
        cur.val=True

    def check(self, word: str):
        cur = self.root
        for c in word:
            cur = cur.check(c)
            if not cur:
                break
        return cur


def initBoard(board: list):
    X = " " * len(board[0])
    for i, e in enumerate(board):
        board[i] = "".join(e) + " "
    board.append(X)


class Solution:
    def __init__(self):
        self.words = None
        self.found: set = set()
        self.board = None

    def getNeigh(self, i, j):
        return {(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)}

    def dfs(self, mi, mj, node: Node):
        if node.val:
            self.found.add(''.join(self.word))
        self.visited.add((mi, mj))
        for nex in self.getNeigh(mi, mj):
            if nex in self.visited:
                continue
            i, j = nex
            cval = self.board[i][j]
            nexnode = node.check(cval)
            if nexnode:
                self.word.append(cval)
                self.dfs(i, j, nexnode)
                self.word.pop()
        self.visited.remove((mi, mj))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        self.words = WordDict()
        root = self.words.root
        while words:
            self.words.add(words.pop())
        self.board = board
        initBoard(board)
        self.found = set()
        self.word = []
        self.visited = set()
        for i in range(n):
            E = board[i]
            for j in range(m):
                e = E[j]
                node = root.check(e)
                if node:
                    self.word.append(e)
                    self.dfs(i,j, node)
                    self.word.pop()
        return list(self.found)

    main = findWords


TESTS = [
    (
        ([["o", "a", "a", "col_lim"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
         ["oath", "pea", "eat", "rain"]),
        ["oath", "eat"])
    ,
    (
        ([["a", "a"]], ['aaa']),
        []
    )
    ,
    (
        (
            [['a'] for i in range(30)],
            ['aaaaa', 'a']
        ),
        ['aaaaa', 'a']
    )
]


def do_tests(tests, only_show_errors=False):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    for i, (args, true_res) in enumerate(tests):
        res = SOL.main(*args)
        count += set(res) == set(true_res)
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

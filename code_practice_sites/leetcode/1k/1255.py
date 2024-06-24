from typing import *


def toIndex(c):
    return ord(c) - 97


def ListToDict(L):
    counter = {e: 0 for e in L}
    for e in L:
        counter[e] += 1
    return counter


def trySubtract(A: dict, B: dict):
    C = A.copy()
    for e, v in B.items():
        if e not in C or v > C[e]:
            return None
        C[e] -= v
    return C


class Solution:
    def __init__(self):
        self.stack = None
        self.score = None
        self.ind = -1

    def getNumber(self):
        self.ind += 1
        return self.ind

    def processWord(self, word):
        word = ListToDict(word)
        score = 0
        for e, v in word.items():
            if e not in self.score:
                return {e: 1}, -1
            score += v * self.score[e]
        return word, score

    def step(self, word):
        word, score = self.processWord(word)
        for i in range(len(self.stack)):
            value, counter = self.stack[i]
            newcounter = trySubtract(counter, word)
            if newcounter:
                self.stack.append((value+score, newcounter))
        return

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters = ListToDict(letters)
        score = {e: score[toIndex(e)] for e in letters}
        self.ind = -1
        self.score = score
        self.stack: list[tuple[int, dict]] = [(0, letters)]
        while words:
            self.step(words.pop())
        best = 0
        while self.stack:
            res, _ = self.stack.pop()
            if res > best:
                best = res
        return best

    main = maxScoreWords


def test():
    inp=(
        ["dog", "cat", "dad", "good"],
        ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    )
    return inp, 23


def main():
    SOL = Solution()
    args, true_res = test()
    res = SOL.main(*args)
    print("Got {} ({})".format(res, type(res)))
    print("Expected {} ({})".format(true_res, type(true_res)))
    return


if __name__ == "__main__":
    main()

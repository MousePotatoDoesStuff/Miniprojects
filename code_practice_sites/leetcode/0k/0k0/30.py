import heapq
from collections import defaultdict, deque
from typing import List


def getOccurences(s, words):
    starters = {e[0]: [] for e in words}
    for i, e in enumerate(words):
        starters[e[0]].append(i)
    Q = []
    res = [set() for e in words]
    for i, e in enumerate(s+"_"):
        NQ = []
        for key in starters.get(e, []):
            NQ.append((key, i))
        while Q:
            key, ind = Q.pop()
            word = words[key]
            i2 = i - ind
            if i2 == len(word):
                res[key].add(ind)
                continue
            if word[i2] != e:
                continue
            NQ.append((key, ind))
        Q = NQ
    return res


def arrangeJumps(occurences, wordLengths):
    jumps = dict()
    for i, E in enumerate(occurences):
        n = wordLengths[i]
        for ind in E:
            jumps[ind] = (i, ind + n)
    return jumps


def checkConcat(jumps: dict, wordRepeats: list, wordCount: int, windowSize: int):
    jumpPoints = list(jumps.keys())
    jumpPoints.sort()
    jumpD = dict()
    RES = []
    for e in jumpPoints:
        wID, nex = jumps[e]
        (curQ, curD) = jumpD.pop(e, (deque(), defaultdict(int)))
        curD[wID] += 1
        curQ.append(wID)
        while curD[wID] > wordRepeats[wID]:
            curD[curQ.popleft()] -= 1
        if len(curQ) == wordCount:
            RES.append(nex - windowSize)
        jumpD[nex] = (curQ, curD)
    return RES


def makeUnique(words):
    uniqueWords = list(set(words))
    uniqueWords.sort()
    wordRepeats = [0 for e in uniqueWords]
    words.sort()
    curind = 0
    for e in words:
        if uniqueWords[curind] != e:
            curind += 1
        wordRepeats[curind] += 1
    return uniqueWords, wordRepeats


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen=len(words[0])
        uniqueWords, wordRepeats = makeUnique(words)
        occurences = getOccurences(s, uniqueWords)
        wordLengths = [len(e) for e in uniqueWords]
        jumps = arrangeJumps(occurences, wordLengths)
        wordCount=sum(wordRepeats)
        RES = checkConcat(jumps, wordRepeats, wordCount, wordlen*wordCount)
        return RES


def main():
    sol = Solution()
    res = sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
    print(res)
    return


if __name__ == "__main__":
    main()

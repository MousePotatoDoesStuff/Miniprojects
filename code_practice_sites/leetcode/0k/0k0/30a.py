import heapq
from collections import defaultdict, deque
from typing import List


def getOccurences(s, words):
    starters = {e[0]: [] for e in words}
    for i, e in enumerate(words):
        starters[e[0]].append(i)
    Q = []
    res = [set() for e in words]
    for i, e in enumerate(s):
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

def arrangeJumps(occurences,wordLengths):
    jumps=defaultdict(list)
    for i,E in enumerate(occurences):
        n=wordLengths[i]
        for ind in E:
            jumps[ind].append((i,ind+n))
    starters={e for e in jumps if e not in jumps.values()}
    return jumps,starters



def checkConcat(jumps:dict,wordRepeats:list,fullSize:int):
    jumpPoints=list(jumps.keys())
    jumpPoints.sort()
    for e in jumpPoints:
        X=[set()]





def makeUnique(words):
    uniqueWords=list(set(words))
    uniqueWords.sort()
    wordRepeats=[0 for e in uniqueWords]
    words.sort()
    curind=0
    for e in words:
        if uniqueWords[curind]!=e:
            curind+=1
        wordRepeats[curind]+=1
    return uniqueWords,wordRepeats



class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:z
        uniqueWords, wordRepeats = makeUnique(words)
        occurences = getOccurences(s, uniqueWords)
        wordLengths=[len(e) for e in uniqueWords]
        jumps=arrangeJumps(occurences,wordLengths)
        total=sum(wordLengths)
        RES=checkConcat(jumps,wordRepeats,total)
        return RES


def main():
    sol=Solution()
    res=sol.findSubstring("barfoothefoobarman",["foo","bar"])
    print(res)
    return


if __name__ == "__main__":
    main()

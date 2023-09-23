from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        D=dict()
        lens=list()
        while len(words)>0:
            e=words.pop()
            n=len(e)
            L=D.get(n,set())
            L.add(e)
            D[n]=L
            lens.append(n)
        lens.sort()


Solution_v1=Solution

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        D=dict()
        lens=list()
        for i,e in enumerate(words):
            n=len(e)
            L=D.get(n,set())
            L.add(i)
            D[n]=L
            lens.append(n)


Solution_v2=Solution


def main():
    return


if __name__ == "__main__":
    main()

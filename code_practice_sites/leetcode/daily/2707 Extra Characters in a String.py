from collections import deque
from typing import List


class Word:
    def __init__(self,word,best,start):
        self.word = word
        self.best = best
        self.start = start
        return
    def __str__(self):
        return str((self.word,self.best,self.start))


class Solution:

    def __init__(self):
        self.words = None
        self.begins = None

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        s += ' '
        self.words = dictionary
        self.begins = {e[0]: set() for e in self.words}
        for i, e in enumerate(dictionary):
            self.begins[e[0]].add(i)
        self.best = 0
        log=deque()
        for i, e in enumerate(s):
            new_words=deque()
            while len(log)>0:
                cur=log.popleft()
                cur:Word
                word=self.words[cur.word]
                if cur.start+len(word)==i:
                    self.best=max(self.best,cur.best+len(word))
                    continue
                if word[i-cur.start]==e:
                    new_words.append(cur)
            for word in self.begins.get(e,[]):
                new_words.append(Word(word,self.best,i))
            log=new_words
            print(self.best,[str(s) for s in log])
        return len(s)-self.best-1

def main():
    s = "leetscode".replace(' ','')
    print(len(s))
    L = ["leet","code","leetcode"]
    res = Solution().minExtraChar(s, L)
    print(res)
    s = "voctv ochpg  utoyw pnafy  lzelq snzsb  andjc qdciy  oefi".replace(' ','')
    print(len(s))
    L = ["tf", "v", "wadrya", "a", "cqdci", "uqfg", "voc", "zelqsn", "band", "b", "yoefi", "utoywp", "herqqn", "umra",
         "frfuyj", "vczatj", "sdww"]
    res = Solution().minExtraChar(s, L)
    print(res)
    return


if __name__ == "__main__":
    main()

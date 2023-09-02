from typing import List


class State:
    def __init__(self, count=0, last=0):
        self.count = count
        self.last = last
        return

    def comp(self, other):
        other: State
        a = self.count - self.last
        b = other.count - other.last
        return int(a > b) - int(a < b)


    def __str__(self):
        return "{}->{}".format(self.last,self.count)


class Solution:
    def __init__(self):
        self.words = []
        self.begins = dict()
        self.states = dict()
        return

    def step(self, ind, char):
        blank: State = self.states[-1]
        for word in set(self.states.keys()) - {-1}:
            state = self.states[word]
            diff = ind - state.last
            if len(self.words[word]) == diff:
                state.last=ind
                if blank.comp(state) > 0:
                    blank = state
                self.states.pop(word)
                continue
            if char != self.words[word][diff]:
                self.states.pop(word)
                continue
        a = blank.count + ind - blank.last
        for word in self.begins.get(char, []):
            self.states[word] = State(a,ind)
        self.states[-1]=blank
        print(ind,"|----|")
        for e in self.states:
            print(e,self.states[e])
        return

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        s += ' '
        self.words = dictionary
        self.begins = {e[0]: set() for e in self.words}
        for i, e in enumerate(dictionary):
            self.begins[e[0]].add(i)
        self.states[-1] = State()
        for (i, e) in enumerate(s):
            self.step(i, e)
        return self.states[-1].count+i-1-self.states[-1].last


def main():
    s="leetscodes"
    L=["leet","code","leetcode"]
    res=Solution().minExtraChar(s,L)
    print(res)
    return


if __name__ == "__main__":
    main()

from typing import List


class State:
    def __init__(self, count=0, word=-1, last=0):
        self.count = count
        self.word = word
        self.last = last
        return

    def comp(self, other):
        other: State
        a = self.count - self.last
        b = other.count - other.last
        return int(a > b) - int(a < b)

    def __str__(self):
        return "{}:{}->{}".format(self.word, self.last, self.count)


class Solution:
    def __init__(self):
        self.words = []
        self.begins = dict()
        self.null = State()
        self.states: List[State] = []
        return

    def step(self, ind, char):
        new_states = []
        while len(self.states) != 0:
            state = self.states.pop()
            word = state.word
            diff = ind - state.last
            if len(self.words[word]) == diff:
                if diff==1:
                    print('???')
                state.last = ind
                if self.null.comp(state) > 0:
                    self.null = state
                continue
            if char == self.words[word][diff]:
                new_states.append(state)
        states=new_states
        a = self.null.count + ind - self.null.last
        for word in self.begins.get(char, []):
            self.states.append(State(a, word, ind))
        return

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        s += ' '
        self.words = dictionary
        self.begins = {e[0]: set() for e in self.words}
        for i, e in enumerate(dictionary):
            self.begins[e[0]].add(i)
        self.null = State()
        for (i, e) in enumerate(s):
            self.step(i, e)
        print(self.null.count,len(s) - 1,self.null.last)
        return self.null.count + len(s) - 1 - self.null.last


def main():
    s = "voctv ochpg  utoyw pnafy  lzelq snzsb  andjc qdciy  oefi".replace(' ','')
    print(len(s))
    L = ["tf", "v", "wadrya", "a", "cqdci", "uqfg", "voc", "zelqsn", "band", "b", "yoefi", "utoywp", "herqqn", "umra",
         "frfuyj", "vczatj", "sdww"]
    res = Solution().minExtraChar(s, L)
    print(res)
    return


if __name__ == "__main__":
    main()

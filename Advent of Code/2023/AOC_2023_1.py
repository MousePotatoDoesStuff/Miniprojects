from pathlib import Path


class NFA_state:
    def __init__(self, ID, value=None):
        self.ID=ID
        self.next = dict()
        self.value = value
        return

    def add(self, key, order):
        if key in self.next:
            return self.next[key]
        new=order()
        self.next[key] = new
        return new


class NFA:
    def __init__(self):
        self.count=0
        self.start = self.add_state()
        self.states=[self.start]
        return

    def add_state(self):
        new=NFA_state(self.count)
        self.count+=1
        return new

    def add_word(self, word, value):
        last = self.start
        for e in word:
            last = last.add(e,self.add_state)
        last.value = value
        return

    def print(self):
        L=[(self.start,"Start",0)]
        while L:
            cur:NFA_state
            cur,e,ofs=L.pop()
            print("-|"*ofs,cur.ID,e)
            ofs+=1
            for e,v in cur.next.items():
                L.append((v,e,ofs))
        return

    def get_states(self):
        return [e.ID for e in self.states]

    def reset(self):
        self.states=[self.start]

    def step(self,key):
        L=[self.start]
        values=[]
        for state in self.states:
            state:NFA_state
            if key in state.next:
                nexstate:NFA_state=state.next[key]
                if nexstate.value is not None:
                    values.append(nexstate.value)
                L.append(nexstate)
        self.states=L
        return values

    def process(self,s,resetOnFound=True):
        self.reset()
        res=[]
        for e in s:
            val=self.step(e)
            if val:
                res.append(val[0])
                if resetOnFound:
                    self.reset()
        return res



def convert_to_numbers(s):
    N = NFA()
    S = "one, two, three, four, five, six, seven, eight, nine".split(", ")
    for i,e in enumerate(S):
        N.add_word(e, i+1)
        N.add_word(str(i+1), i+1)
    # N.print()
    res=N.process(s)
    res2=N.process(s,False)
    if res[0]!=res2[0] or res[-1]!=res2[-1]:
        print(s,res,res2)
    return res


def solve(IN):
    res = 0
    for E in IN.split("\n"):
        if data['version'] == 2:
            tres=convert_to_numbers(E)
            res+=tres[0]*10+tres[-1]
        else:
            first = ""
            last = ""
            for e in E:
                if e in "1234567890":
                    if first == "":
                        first = e
                    last = e
            res += int('0' + first + last)
    return res


in_loc = "AOC_2023_{}.txt"
data = {'version': 2}


def main():
    num = Path(__file__).name.split('_')[-1][:-3]
    F = open(in_loc.format(num), 'r')
    IN = F.read()
    F.close()
    OUT = solve(IN)
    print(OUT)
    return


if __name__ == "__main__":
    main()

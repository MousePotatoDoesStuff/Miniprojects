class charlog:
    def __init__(self, s):
        v = set(s)
        self.chars = {e: 0 for e in v}
        self.unsatisfied = len(v)
        for e in s:
            self.chars[e] -= 1
        return
    def __str__(self):
        s=str(self.unsatisfied)
        L=[e+"+-"[v<0]+str(abs(v)) for(e,v) in self.chars.items()]
        return " [{}] ".format(s+": "+",".join(L))

    def add(self, s):
        for e in s:
            if e not in self.chars:
                continue
            print(str(self),end='+')
            print(e,end='=')
            self.chars[e] += 1
            if self.chars[e] == 0:
                self.unsatisfied -= 1
            print(str(self))
        return

    def sub(self, s):
        for e in s:
            print(str(self),end='-')
            if e not in self.chars:
                self.chars[e] = 0
            print(e,end='=')
            self.chars[e] -= 1
            if self.chars[e] == -1:
                self.unsatisfied += 1
            print(str(self))
        return


def MinWindowSubstring(strArr):
    L = strArr[2:][:-2].split('", "')
    s = L[0]
    n = len(s)
    start = 0
    CL = charlog(L[1])
    for end in range(0, n):
        CL.add(s[end])
        while CL.unsatisfied == 0:
            CL.sub(s[start])
            start += 1
        print(start,end+1,s[start:end+1])
    return strArr


def main():
    print(MinWindowSubstring('["ahffaksfajeeubsne", "jefaa"]'))


if __name__ == "__main__":
    main()

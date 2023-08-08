class charlog:
    def __init__(self, s):
        v = set(s)
        self.chars = {e: 0 for e in v}
        self.unsatisfied = len(v)
        for e in s:
            self.chars[e] -= 1
        return

    def add(self, s):
        for e in s:
            if e not in self.chars:
                continue
            self.chars[e] += 1
            if self.chars[e] == 0:
                self.unsatisfied -= 1
        return

    def sub(self, s):
        for e in s:
            if e not in self.chars:
                self.chars[e] = 0
            self.chars[e] -= 1
            if self.chars[e] == -1:
                self.unsatisfied += 1
        return


def MinWindowSubstring(strArr):
    L = strArr[2:][:-2].split('", "')
    s = L[0]
    n = len(s)
    start=0
    CL=charlog(L[1])
    for end in range(0,n):
        CL.add(s[end])
        while CL.unsatisfied==0:
            CL.sub(s[start])
            print(s[start:end],end='->')
            start+=1
        print('|')

    return strArr


def main():
    print(MinWindowSubstring('["ahffaksfajeeubsne", "jefaa"]'))


if __name__ == "__main__":
    main()

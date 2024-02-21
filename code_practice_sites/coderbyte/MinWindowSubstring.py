class charlog:
    def __init__(self, s):
        v = set(s)
        self.chars = {e: 0 for e in v}
        self.unsatisfied = len(v)
        for e in s:
            self.chars[e] -= 1
        return

    def __str__(self):
        s = str(self.unsatisfied)
        L = [e + "+-"[v < 0] + str(abs(v)) for (e, v) in self.chars.items()]
        return " [{}] ".format(s + ": " + ",".join(L))

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
                return
            self.chars[e] -= 1
            if self.chars[e] == -1:
                self.unsatisfied += 1
        return


def MinWindowSubstring(strArr):
    s = strArr[0]
    n = len(s)
    start = 0
    CL = charlog(strArr[1])
    best = (n + 1, '')
    for end in range(0, n):
        CL.add(s[end])
        if CL.unsatisfied == 0:
            while CL.unsatisfied == 0:
                CL.sub(s[start])
                start += 1
            if best[0] > end + 2 - start:
                best = end + 2 - start, s[start - 1:end + 1]
    return best[1]


def main():
    print(MinWindowSubstring(["ab  c    ", "abc"]))


if __name__ == "__main__":
    main()

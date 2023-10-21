class SlidingMax:
    def __init__(self, L, k):
        self.M = [L]
        self.k = k
        cur = L
        while len(cur) > 0:
            L2 = []
            c2 = None
            k2 = 0
            for e in cur:
                if not c2 or e > c2:
                    c2 = e
                k2 += 1
                if k2 == k:
                    L2.append(c2)
                    c2 = None
                    k2 = 0
            cur = L2
            self.M.append(L2)
        self.M.pop()

    def change(self, index, value):
        if index not in range(len(self.M[0])):
            return False
        for level, L in enumerate(self.M):
            if len(L) < self.k:
                L[index] = value
                return
            new, rem = divmod(index, self.k)
            a = index - rem
            L[index] = value
            value = self.check(level, a, a + self.k, value)
            index //= self.k

    def check(self, level, start, end, res):
        L = self.M[level]
        for i in range(start, end):
            if res < L[i]:
                res = L[i]
        return res

    def getmax(self, start, end):
        if end > len(self.M[0]):
            end = len(self.M[0])
        if start < 0:
            start = 0
        res = self.M[0][start]
        for level in range(len(self.M)):
            firstlim = start - (start % self.k) + self.k
            secondlim = end - (end % self.k)
            if firstlim >= secondlim:
                if start < end:
                    res = self.check(level, start, end, res)
                return res
            res = self.check(level, start, firstlim, res)
            res = self.check(level, secondlim, end, res)
            start = firstlim // self.k
            end = secondlim // self.k


def main():
    X = SlidingMax([1,-1,-1,2,5,6,3,4,5],3)
    for i in range(9):
        print(X.getmax(i-3,i))


if __name__ == "__main__":
    main()

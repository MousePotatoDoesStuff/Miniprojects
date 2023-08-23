class Solution:
    def reorganizeString(self, s: str) -> str:
        D = {e:0 for e in s}
        for e in s:
            D[e] += 1
        RD = dict()
        n = len(s)
        N = set()
        for (e, v) in D.items():
            L = RD.get(v, [])
            RD[v] = L
            L.append(e)
            N.add(v)
        D=None
        N=list(N)
        N.sort()
        if N[-1] > (n + 1) // 2:
            return ""
        X = ['' for i in range(n)]
        cur = 0
        while len(N) > 0:
            cn = N.pop()
            for c in RD[cn]:
                for i in range(cn):
                    X[cur] = c
                    cur += 2
                    if cur >= n:
                        cur = 1
        return "".join(X)


def main():
    s="eqmeyggvp"
    res=Solution().reorganizeString(s)
    print("->",res,"<-",sep='')
    return


if __name__ == "__main__":
    main()

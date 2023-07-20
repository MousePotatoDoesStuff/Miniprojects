import math


def MakePerm(X):
    M = [[]]
    for E in X:
        N = []
        for F in M:
            N.extend([F + [e] for e in E])
        M = N
    return M


def LimitedPerm(X, Y, null=None):
    n = len(X)
    M = [[]]
    for i in range(n):
        if Y[i] is not null:
            y = Y[i]
            for E in M:
                E.append(y)
            continue
        N = []
        for F in M:
            N.extend([F + [e] for e in X[i]])
        M = N
    return M


class BaseProb:
    def getValues(self, X: dict):
        raise NotImplementedError


class Prob:
    def __init__(self, variables: list, values):
        self.variables = variables
        self.n = len(variables)
        if type(values) == list:
            P = MakePerm(self.variables)
            if len(values) > len(P):
                values = values[:len(P)]
            elif len(values) < len(P):
                values += [0] * (len(P) - len(values))
            self.values = dict()
            for i in range(len(values)):
                self.values[tuple(P[i])] = values[i]
        return

    def getV(self, X: dict):
        NX = [None]*self.n
        for (e, v) in X.items():
            NX[e] = v
        LP = LimitedPerm(self.variables, NX)
        res = 0
        for E in LP:
            T = tuple(E)
            res += self.values[T]
        return res

    def mutualinfo(self,a,b):
        PAB=dict()
        for va in self.variables[a]:
            for vb in self.variables[b]:
                PAB[(va,vb)]=self.getV({a:va,b:vb})
        PA={va:0 for va in self.variables[a]}
        PB={va:0 for va in self.variables[b]}
        for ((va,vb),p) in PAB.items():
            PA[va]+=p
            PB[vb]+=p
        res=0
        for va in self.variables[a]:
            for vb in self.variables[b]:
                pa=PA[va]
                pb=PB[vb]
                pab=PAB[(va,vb)]
                lnres=math.log(pab)-math.log(pa)-math.log(pb)
                locres=pab*lnres
                res+=locres
                print(a,b,'|',va,vb,'|',pa,pb,pab,lnres,locres)
        return res



def main():
    var = [(0, 1), (0, 1), (0, 1)]
    val = [0.1, 0.0, 0.0, 0.1, 0.1, 0.1, 0.4, 0.2]
    pr = Prob(var, val)
    print(pr.getV({0: 0}))
    print(pr.getV({0: 0, 1: 1}))
    print(pr.getV({0: 0, 1: 0}))
    print(pr.mutualinfo(0,1))
    print(pr.mutualinfo(0,2))
    print(pr.mutualinfo(1,2))
    return


if __name__ == "__main__":
    main()

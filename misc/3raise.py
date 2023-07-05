from typing import List


class RelV:
    def __init__(self, const, x1, n):
        self.const = const
        self.x1 = x1
        self.n = n

    def __iadd__(self, other):
        self.const += other.const
        self.x1 += other.x1
        self.n +=other.n
        return self

    def __isub__(self, other):
        self.const -= other.const
        self.x1 -= other.x1
        self.n -=other.n
        return self

    def __add__(self, other):
        return RelV(self.const + other.const, self.x1 + other.x1, self.n+other.n)

    def __sub__(self, other):
        return RelV(self.const - other.const, self.x1 - other.x1, self.n-other.n)

    def __repr__(self):
        return "{}|{}|{}".format(self.const, self.x1, self.n)



def calculate_values(L):
    L: List[RelV]
    X = [RelV(0, 1, 0)]
    X.append(L[0] - X[0])
    for i in range(1, len(L) - 1):
        N=L[i] - X[-1] - X[-2]
        X.append(N)
    return X, X[-1] + X[-2] - L[-1]


def get_step(a, b, s):
    return -((b - a) / s)


def get_steps(step, L, maxvalue):
    missing = [RelV(maxvalue - e, 0, 1) for e in L]
    V,E=calculate_values(missing)
    print(V)
    print(E)
    if E.x1==0:
        if E.const!=0:
            return -1
    return 0


def main():
    res=get_steps(1, [1,1,1,2],1)
    print(res)
    return


if __name__ == "__main__":
    main()

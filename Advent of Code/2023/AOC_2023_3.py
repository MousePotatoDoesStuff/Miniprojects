from collections import deque
from pathlib import Path


def identify(line, notit, swc):
    key = lambda e: e == '*'
    if swc:
        key = lambda e: e not in notit
    return [i for i, e in enumerate(line) if key(e)] + [10000]


def solve(IN):
    swc = data.get('version') == 1
    print(swc)
    notit = set("0123456789.")
    print(set(IN) - notit)
    IN = IN.split("\n")
    m = len(IN[0]) + 2
    lim = "." * m
    IN = [lim] + ['.' + e + '.' for e in IN] + [lim]
    Q = deque()
    Q.append([1000])
    Q.append([1000])
    Q.append([1000])
    adj = []
    skip = None
    for E in IN:
        Q.append(identify(E, notit, swc))
        Q.popleft()
        curadj = ""
        curind = [0] * 3
        for i in range(m):
            check = False
            for j in range(3):
                e = curind[j]
                while Q[j][e] < i - 1:
                    e += 1
                if Q[j][e] < i + 2:
                    check = True
                curind[j] = e
            if check:
                curadj += "+"
            else:
                curadj += " "
        if skip is None:
            skip = curadj
            continue
        adj.append(curadj)
    adj.append(skip)
    print(len(IN[0]), len(adj[0]))
    notit.remove('.')
    res = 0
    check = []
    for i, E in enumerate(IN):
        chl = ''
        chlt = ''
        curnum = 0
        ack = False
        for j, e in enumerate(E):
            if e in notit:
                curnum *= 10
                curnum += int(e)
                if not ack and adj[i][j] == "+":
                    ack = True
                chlt += e
                continue
            if curnum != 0:
                if ack:
                    res += curnum
                    chl += chlt
                    ack = False
                else:
                    chl += '.' * len(chlt)
                chlt = ''
                curnum = 0
            chl += ['*X', ' +'][e == '.'][adj[i][j] == '+']
        check.append(chl)
    print("\n".join(check))
    return res


def solve2(IN):
    IN = IN.split("\n")
    m = len(IN[0]) + 2
    lim = "." * m
    IN = [lim] + ['.' + e + '.' for e in IN] + [lim]
    adj = dict()
    resnums = dict()
    count = dict()
    for i, E in enumerate(IN):
        for j, F in enumerate(E):
            if F == "*":
                S1 = (i, j)
                resnums[S1] = 1
                count[S1]=0
                for k1 in range(-1, 2):
                    for k2 in range(-1, 2):
                        S2 = (i + k1, j + k2)
                        TS = adj.get(S2, set())
                        TS.add(S1)
                        adj[S2] = TS
    print(adj)
    notit = set("0123456789")
    for i, E in enumerate(IN):
        curnum = 0
        ack = set()
        for j, e in enumerate(E):
            if e in notit:
                curnum *= 10
                curnum += int(e)
                if (i, j) in adj:
                    ack |= adj[(i, j)]
                continue
            if curnum != 0:
                if ack:
                    for E in ack:
                        resnums[E] *= curnum
                        count[E]+=1
                    ack = set()
                curnum = 0
    D=dict()
    for e in count.values():
        D[e]=D.get(e,0)+1
    res=0
    res2=0
    for e in count:
        res2+=resnums[e]
        if count[e]<2:
            print(count[e],e,resnums[e])
            continue
        res+=resnums[e]
    return res,res2


in_loc = "AOC_2023_{}.txt"
data = {'version': 2}


def main():
    num = Path(__file__).name.split('_')[-1][:-3]
    F = open(in_loc.format(num), 'r')
    IN = F.read()
    F.close()
    OUT = solve2(IN)
    print(OUT)
    return


if __name__ == "__main__":
    main()

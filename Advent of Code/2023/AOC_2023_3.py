from collections import deque
from pathlib import Path


def identify(line, notit):
    return [i for i, e in enumerate(line) if e not in notit] + [10000]


def solve(IN):
    IN = IN.split("\n")
    m = len(IN[0])
    lim = "." * m
    IN = [lim] + ['.' + e + '.' for e in IN] + [lim]
    notit = set("0123456789.")
    Q = deque()
    Q.append([1000])
    Q.append([1000])
    Q.append([1000])
    res = 0
    adj = []
    for E in IN:
        print(E)
        Q.append(identify(E, notit))
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
        adj.append(curadj)
    notit.remove('.')
    res=0
    for i,E in enumerate(IN):
        curnum=0
        ack=False
        for j,e in enumerate(E):
            if e in notit:
                curnum*=10
                curnum+=int(e)
                if not ack and adj[i][j]:
                    ack=True
            elif curnum!=0:
                if ack:
                    res+=curnum
                curnum=0
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

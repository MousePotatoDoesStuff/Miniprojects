from pathlib import Path


def solve(IN):
    lim="."*len(IN[0])
    IN=[lim]+['.'+e+'.' for e in IN]+[lim]
    n=len(IN)
    m=len(IN[0])
    notit=set("0123456789.")
    neigh=set()
    for i in range(-1,2):
        for j in range(-1,2):
            neigh.add((i,j))
    neigh.remove((0,0))
    used=set()
    for i,E in enumerate(IN):
        for j,e in enumerate(E):
            if e not in notit:
                for k,k2 in neigh:
                    used.add((i+k,j+k2))
    notit.remove('.')
    res=0
    for e in used:
        E=IN[e[0]][e[1]]
        if E in notit:
            res+=int(E)
    return res


in_loc = "AOC_2023_{}.txt"
data = {'version': 2}


def main():
    num=Path(__file__).name.split('_')[-1][:-3]
    F=open(in_loc.format(num),'r')
    IN=F.read()
    F.close()
    OUT = solve(IN)
    print(OUT)
    return


if __name__ == "__main__":
    main()

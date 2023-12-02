from pathlib import Path

def decipher(gameRaw):
    game=gameRaw.split(": ")
    gameID=int(game[0][5:])
    game=game[1].split("; ")
    res={e:0 for e in 'rgb'}
    for E in game:
        F=E.split(', ')
        temp={e:0 for e in 'rgb'}
        for f in F:
            G=f.split(' ')
            temp[G[1][0]]+=int()
        for e,v in temp.items():
            res[e]=max(res[e],v)
    return res
def checkIfFits(game:dict,ref:dict):
    for e,v in game.items():
        if v>ref.get(e,0):
            return False
    return True


def solve(IN):
    L=IN.split("\n")
    print(decipher(L[0]))
    return IN


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

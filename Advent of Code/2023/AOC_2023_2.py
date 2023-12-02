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
            temp[G[1][0]]+=int(G[0])
        for e,v in temp.items():
            res[e]=max(res[e],v)
    return gameID,res
def checkIfFits(game:dict,ref:dict):
    for e,v in game.items():
        if v>ref.get(e,0):
            return False
    return True


def solve(IN):
    L=IN.split("\n")
    ref={'r':12,'g':13,'b':14}
    res=0
    mode=data.get('version',0)
    for gameRaw in L:
        gameID,game=decipher(gameRaw)
        if mode==1:
            if checkIfFits(game,ref):
                res+=gameID
        else:
            temp=1
            for e in game.values():
                temp*=e
            res+=temp
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

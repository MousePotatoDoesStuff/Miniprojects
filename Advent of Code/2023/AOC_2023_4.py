from collections import deque
from pathlib import Path


def decipher_card(raw):
    L=raw.split('\n')
    RES=[]
    for Eraw in L:
        E=" "+Eraw[10:].replace("  "," ")
        E=E[1:].split(" | ")
        E=[[int(e) for e in F.split(" ") if e] for F in E]
        RES.append(E)
    return RES


def solve1(IN):
    TEMP=decipher_card(IN)
    res=0
    for (A,B) in TEMP:
        C=set(A)&set(B)
        print(C,end="")
        rest=len(C)
        if rest!=0:
            res+=1<<(rest-1)
    print()
    return res

def solve2(IN):
    TEMP=decipher_card(IN)
    winners=[len(set(A)&set(B)) for (A,B) in TEMP]
    print(max(winners))
    Q=deque()
    for i in range(10):
        Q.append(1)
    res=0
    for i,e in enumerate(winners):
        cur=Q.popleft()
        res+=cur
        Q.append(1)
        if cur==0:
            continue
        for j in range(e):
            Q[j]+=cur
        print(i,Q)
    return res

in_loc = "AOC_2023_{}.txt"
data = {'version': 2}


def main():
    num=Path(__file__).name.split('_')[-1][:-3]
    F=open(in_loc.format(num),'r')
    IN=F.read()
    F.close()
    OUT1 = solve1(IN)
    print(OUT1)
    OUT2 = solve2(IN)
    print(OUT2)
    return


if __name__ == "__main__":
    main()

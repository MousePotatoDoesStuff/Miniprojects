from pathlib import Path


def solve(IN):
    res=0
    for E in IN.split("\n"):
        first=""
        last=""
        for e in E:
            if e in "1234567890":
                if first=="":
                    first=e
                last=e
        res+=int('0'+first+last)
    return res


in_loc = "AOC_2023_{}.txt"


def main():
    num=Path(__file__).name.split('_')[-1][:-3]
    F=open(in_loc.format(num),'r')
    IN=F.read()
    F.close()
    OUT = solve(IN)
    print(OUT)
    return
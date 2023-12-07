from pathlib import Path

def process_map(IN):
    L=IN.split(" ")
    RES=[]
    for s in L:
        E=[int(e) for e in s.split()]
        RES=

def solve1(IN):
    return "TEST"

def solve2(IN):
    return "MIKE CHECK"

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
